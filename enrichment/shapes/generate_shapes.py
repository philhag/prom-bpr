import csv
import re
import glob
import os

# passende CSV-Dateien suchen (optional: Pattern einschränken)
csv_files = glob.glob("mapping_*.csv")

if not csv_files:
    raise FileNotFoundError("Keine passenden CSV-Dateien gefunden.")

# zuletzt geänderte Datei bestimmen
csv_file = max(csv_files, key=os.path.getmtime)

output_file = "generated_shapes.ttl"
SKIP_UNASSIGNED = False

prefixes = """@prefix sh:    <http://www.w3.org/ns/shacl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix prom:  <https://w3id.org/prom-bpr#> .

"""

# Regex-Sonderzeichen
REGEX_META = re.compile(r'[.\^$*+?{}\[\]\\|()]')

def turtle_escape(s: str) -> str:
    """Escaped einen String für Turtle in Doppel-Anführungszeichen."""
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    return s

def contains_regex_meta(s: str) -> bool:
    """Prüft, ob Regex-Sonderzeichen im String vorkommen."""
    return bool(REGEX_META.search(s))

seen_labels = set()

with open(csv_file, newline="", encoding="utf-8") as csvfile, \
     open(output_file, "w", encoding="utf-8") as out:

    reader = csv.DictReader(csvfile, delimiter=';')
    out.write(prefixes)
    not_assigned_count = 0
    shape_counter = 1
    row_count = 0;
    skipped_count = 0;
    for row in reader:
        row_count += 1
        print(f"----------------------------------------------")
        print(f"Processing row {row_count}: {row}")
        
        label = row['EventLogLabel'].replace('*', '').strip()

        if ':' in label:
            label = label.split(':', 1)[0].strip()

        if label in seen_labels:
            print(f"Skip {row_count}")
            skipped_count += 1
            continue
        seen_labels.add(label)
        
        
        activity_url = row['ActivityURL']
        if activity_url == "#NV" or activity_url.strip() == "":
            activity_url = "https://w3id.org/prom-bpr#UnclassifiedEventLogEntry"
            print(f"Not assigned row: {row_count}")
            not_assigned_count += 1
            if SKIP_UNASSIGNED:
                continue
        print(f"Label: '{label}', Activity URL: '{activity_url}'")
        #label_ttl = turtle_escape(label)

        # -------------------------------------------------
        # FALL 1: Label enthält Regex-Metazeichen
        # → nur hasValue
        # -------------------------------------------------
        if contains_regex_meta(label):

            shape = f"""
prom:Shape_{shape_counter}
    a sh:NodeShape ;
    sh:targetClass prom:EventLogEntry ;
    sh:rule [
        a sh:TripleRule ;
        sh:condition [
            sh:property [
                sh:path rdfs:label ;
                sh:hasValue "{label}" ;
            ]
        ] ;
        sh:subject sh:this ;
        sh:predicate rdf:type ;
        sh:object <{activity_url}> ;
    ] .
"""
            out.write(shape)
            shape_counter += 1

        # -------------------------------------------------
        # FALL 2: kein Regex-Sonderzeichen
        # → pattern + hasValue
        # -------------------------------------------------
        else:

            # 2a) pattern-Shape
            shape_pattern = f"""
prom:Shape_{shape_counter}
    a sh:NodeShape ;
    sh:targetClass prom:EventLogEntry ;
    sh:rule [
        a sh:TripleRule ;
        sh:condition [
            sh:property [
                sh:path rdfs:label ;
                sh:pattern "{label}" ;
                sh:flags "i" ;
            ]
        ] ;
        sh:subject sh:this ;
        sh:predicate rdf:type ;
        sh:object <{activity_url}> ;
    ] .
"""
            out.write(shape_pattern)
            shape_counter += 1

            # 2b) hasValue-Shape
            shape_hasvalue = f"""
prom:Shape_{shape_counter}
    a sh:NodeShape ;
    sh:targetClass prom:EventLogEntry ;
    sh:rule [
        a sh:TripleRule ;
        sh:condition [
            sh:property [
                sh:path rdfs:label ;
                sh:hasValue "{label}" ;
            ]
        ] ;
        sh:subject sh:this ;
        sh:predicate rdf:type ;
        sh:object <{activity_url}> ;
    ] .
"""
            out.write(shape_hasvalue)
            shape_counter += 1
print(f"Anzahl Zeilen mit nicht zugeordnetem Label: {not_assigned_count}")
print(f"Anzahl Zeilen mit bereits gesehenem Label (skipped): {skipped_count}")
print(f"Anzahl Zeilen mit verarbeitetem Label: {row_count - not_assigned_count - skipped_count}")

print(f"{shape_counter-1} SHACL Shapes wurden in {output_file} geschrieben.")
