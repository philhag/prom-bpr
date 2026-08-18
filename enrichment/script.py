# python -m pip install package_name 
from itertools import islice
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS
from pyshacl import validate
import pm4py
import uuid
import rdflib
import copy
import os
from pm4py.objects.log.exporter.xes import exporter as xes_exporter
from datetime import datetime

timestamp2 = datetime.now().strftime("%Y-%m-%d")
print("Aktuelles Datum:", timestamp2)
input_folder = "data_in"
output_folder = "data_out"

os.makedirs(output_folder, exist_ok=True)

# Shapes und Ontologien einmal laden
shapes_graph = rdflib.Graph()
shapes_graph.parse("shapes/generated_shapes.ttl", format="turtle")

ont_graph = Graph()
ont_graph.parse("ontologies/prom-bpr.ttl", format="turtle")
ont_graph.parse("ontologies/ontobpr.ttl", format="turtle")

for file in os.listdir(input_folder):

    if not file.endswith(".xes"):
        continue

    xes_file_path = os.path.join(input_folder, file)
    base_name = os.path.splitext(file)[0]

    print("=======================================")
    print("Processing:", xes_file_path)

    xes_log = pm4py.read_xes(xes_file_path)
    print("Anzahl Traces im Event Log:", len(xes_log))

    g = Graph()

    PROM = Namespace("https://w3id.org/prom-bpr#")
    PROV = Namespace("http://www.w3.org/ns/prov#")
    ONTOBPR = Namespace("https://w3id.org/ontobpr#")

    g.bind("prom", PROM)
    g.bind("ontobpr", ONTOBPR)
    g.bind("rdfs", RDFS)
    g.bind("prov", PROV)

    traces = xes_log.groupby("case:concept:name")

    for trace_id, trace_events in traces:

        trace_uri = URIRef(f"https://example.org/case/{trace_id}")
        g.add((trace_uri, RDF.type, PROM.EventLogCase))
        g.add((trace_uri, PROM.hasCaseId, Literal(trace_id)))

        for _, event in trace_events.iterrows():

            event_uri = URIRef(f"https://example.org/event/{event['eventid']}")
            g.add((event_uri, RDF.type, PROM.EventLogEntry))

            if "concept:name" in event:
                g.add((event_uri, RDFS.label, Literal(event["concept:name"])))

            if "lifecycle:transition" in event and "time:timestamp" in event:
                timestamp = event["time:timestamp"].isoformat()

                if event["lifecycle:transition"] == "start":
                    g.add((event_uri, PROV.startedAtTime, Literal(timestamp)))

                elif event["lifecycle:transition"] == "complete":
                    g.add((event_uri, PROV.endedAtTime, Literal(timestamp)))

            for col, val in event.items():

                if val is None or (isinstance(val, float) and str(val) == "nan"):
                    continue

                if col in ["concept:name", "time:timestamp", "lifecycle:transition", "case:concept:name","prombpr"]:
                    continue

                g.add((event_uri, PROM[col.replace(":", "_")], Literal(str(val).replace(".0",""))))

            g.add((trace_uri, PROM.hasEventLogEntry, event_uri))
            g.add((event_uri, PROM.isEventLogEntryOf, trace_uri))

    print("Tripel vor Rule Execution:", len(g))

    working_graph = copy.deepcopy(g)

    conforms, results_graph, results_text = validate(
        data_graph=working_graph,
        shacl_graph=shapes_graph,
        advanced=True,
        js=False,
        debug=False,
        serialize_report_graph=False,
        inplace=True
    )

    generated_triples = working_graph - g

    generated_triples.bind("prom", PROM)
    generated_triples.bind("ontobpr", ONTOBPR)
    generated_triples.bind("prov", PROV)

    print("Rule Tripel:", len(generated_triples))

    # speichern
    output_file_rules = os.path.join(output_folder, f"{timestamp2}_{base_name}_rules.ttl")
    generated_triples.serialize(destination=output_file_rules, format="turtle")

    g_plus_rules = g + generated_triples

    g_plus_rules.bind("prom", PROM)
    g_plus_rules.bind("ontobpr", ONTOBPR)
    g_plus_rules.bind("prov", PROV)

    output_file_combined = os.path.join(output_folder, f"{timestamp2}_{base_name}_combined.ttl")
    g_plus_rules.serialize(destination=output_file_combined, format="turtle")

    # Composition
    for trace in g_plus_rules.subjects(RDF.type, PROM.EventLogCase):

        events = list(g_plus_rules.objects(trace, PROM.hasEventLogEntry))

        type_map = {}

        for event in events:
            for cls in g_plus_rules.objects(event, RDF.type):

                if cls in (PROM.EventLogEntry, PROM.UnclassifiedEventLogEntry):
                    continue

                type_map.setdefault(cls, []).append(event)

        for cls, evs in type_map.items():

            compound_uri = URIRef(f"https://example.org/compound/{uuid.uuid4()}")

            g_plus_rules.add((compound_uri, RDF.type, PROM.EventLogCompound))
            g_plus_rules.add((compound_uri, RDF.type, cls))

            for ev in evs:
                g_plus_rules.add((compound_uri, PROM.hasEventLogEntry, ev))
                g_plus_rules.add((compound_uri, PROM.hasCase, trace))
                g_plus_rules.add((ev, PROM.isEventLogEntryOf, compound_uri))

    output_file_composition = os.path.join(output_folder, f"{timestamp2}_{base_name}_composition.ttl")
    g_plus_rules.serialize(destination=output_file_composition, format="turtle")

    # XES Enrichment
    query = """
    PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX prom: <https://w3id.org/prom-bpr#>

    SELECT ?eventid ?pmclass
    WHERE {
        ?event rdf:type ?pmclass ;
               prom:eventid ?eventid .

        FILTER(STRSTARTS(STR(?pmclass), "https://w3id.org/prom-bpr#"))

        FILTER(?pmclass NOT IN (
            prom:EventLogEntry,
            prom:UnclassifiedEventLogEntry,
            prom:EventLogCompound,
            prom:EventLogCase
        ))
    }
    """

    log_old = pm4py.read_xes(xes_file_path, return_legacy_log_object=True)

    event_class_map = {}

    for row in g_plus_rules.query(query):

        event_id = str(row.eventid)
        cls = str(row.pmclass)

        if event_id not in event_class_map:
            event_class_map[event_id] = cls

    enriched_log = copy.deepcopy(log_old)

    for trace in enriched_log:
        for event in trace:

            event_id = str(event.get("eventid"))

            if event_id in event_class_map:
                full_value = event_class_map[event_id]

                # Teil nach #
                short_value = full_value.split("#")[-1]

                # Original sichern
                event["prombpr:originalName"] = event.get("concept:name")

                # neuen Namen setzen
                event["concept:name"] = short_value
                event["prombpr:url"] = event_class_map[event_id]

    output_xes_file = os.path.join(output_folder, f"{timestamp2}_{base_name}_enriched_v3.xes")

    xes_exporter.apply(enriched_log, output_xes_file)

    print("Fertig:", base_name)