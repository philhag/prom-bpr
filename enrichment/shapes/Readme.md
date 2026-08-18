# SHACL Shape Generator

Python script for automatically generating SHACL Triple Rules from a CSV-based event-to-activity mapping.

## Workflow

The script:

1. Searches for files matching `mapping_*.csv`.
2. Selects the most recently modified CSV file.
3. Reads the event labels and corresponding activity URLs.
4. Removes duplicate event labels.
5. Assigns unclassified events to `prom:UnclassifiedEventLogEntry`.
6. Generates SHACL rules for each mapping.
7. Writes the generated shapes to `generated_shapes.ttl`.

For labels without regex metacharacters, both a case-insensitive `sh:pattern` rule and an exact `sh:hasValue` rule are generated. Labels containing regex metacharacters use only `sh:hasValue`.

## Input

The input CSV must contain at least the following columns:

```text
EventLogLabel;ActivityURL
```

Example:

```text
Registration of Application;https://w3id.org/prom-bpr#Registration
Request Documents;https://w3id.org/prom-bpr#RequestFurtherDocuments
```

The CSV files should be located in the same directory as the script and follow the naming pattern:

```text
mapping_*.csv
```

## Output

The script generates:

```text
generated_shapes.ttl
```

The resulting Turtle file contains SHACL NodeShapes targeting:

```text
prom:EventLogEntry
```

and assigns the corresponding PROM-BPR activity class using `sh:TripleRule`.

## Usage

Run the script with:

```bash
python generate_shapes.py
```

No external Python packages are required; the script uses only Python standard-library modules.

## Configuration

The handling of unassigned mappings can be controlled with:

```python
SKIP_UNASSIGNED = False
```

* `False`: generate a rule assigning unclassified events to `prom:UnclassifiedEventLogEntry`.
* `True`: skip unassigned mappings entirely.
