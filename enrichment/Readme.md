# PROM-BPR Event Log Enrichment

Python script for transforming XES event logs into RDF-based representations, validating and enriching them using SHACL rules, creating event-log compositions, and exporting enriched XES logs.

## Workflow

The script performs the following steps:

1. Reads XES event logs from `data_in/`.
2. Converts events and traces into RDF using the PROM-BPR and OntoBPR ontologies.
3. Applies SHACL rules from `shapes/generated_shapes.ttl`.
4. Exports generated rule triples and the combined RDF graph as Turtle.
5. Creates compound event-log entities based on inferred event classes.
6. Enriches the original XES log with PROM-BPR classifications.
7. Writes all results to `data_out/`.

## Directory Structure

```text
.
├── script.py
├── data_in/
│   └── *.xes
├── data_out/
├── ontologies/
│   ├── prom-bpr.ttl
│   └── ontobpr.ttl
└── shapes/
    └── generated_shapes.ttl
```

## Requirements

Python 3.10+ is recommended.

Install the required packages with:

```bash
pip install rdflib pyshacl pm4py
```

Or:

```bash
python -m pip install rdflib pyshacl pm4py
```

## Usage

Place one or more `.xes` event logs in `data_in/` and run:

```bash
python script.py
```

The output files are automatically written to `data_out/` and prefixed with the current date.

For each input log, the script generates:

* `<date>_<name>_rules.ttl` — triples generated through SHACL rule execution
* `<date>_<name>_combined.ttl` — original and rule-generated triples
* `<date>_<name>_composition.ttl` — RDF graph including compound event structures
* `<date>_<name>_enriched_v3.xes` — XES event log enriched with PROM-BPR classifications

## Dependencies

## Dependencies

* **[RDFLib](https://github.com/RDFLib/rdflib)** — RDF graph creation and serialization.  
  Licensed under the **BSD 3-Clause License**.

* **[pySHACL](https://github.com/RDFLib/pySHACL)** — SHACL validation and rule execution.  
  Licensed under the **Apache License 2.0**. 

* **[PM4Py](https://github.com/process-intelligence-solutions/pm4py)** — XES event-log processing and process mining.  
  Licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**. 

These dependencies are third-party software and remain subject to their respective licenses.
* **Python standard library** — UUID generation, file handling, timestamps, and data processing

## Notes

The script expects the input XES logs to contain `case:concept:name` and `eventid` attributes. The referenced ontologies and SHACL shapes must be available at the paths specified above.

## License

This software is released under the **MIT License**. See the [`LICENSE`](LICENSE) file for the full license text.

Copyright © 2026 Philipp Hagedorn
