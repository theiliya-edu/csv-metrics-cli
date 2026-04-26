# csv-metrics-cli

CLI tool for filtering and analyzing video metrics from CSV files.

## Installation

Install dependencies:

```bash
uv sync
```

This will create a virtual environment and install all project dependencies.

---

### Optional: install as CLI command

If you want to use `csv-metrics` as a global CLI command:

```bash
uv pip install -e .
```

After that, you can run:

```bash
csv-metrics --files examples/stats1.csv --report clickbait
```

Otherwise, you can run it via uv:

```bash
uv run csv-metrics --files examples/stats1.csv examples/stats2.csv
```

---

## Input Format

The CLI expects CSV files with the following columns:

```csv
title,ctr,retention_rate,views,likes,avg_watch_time
```

Example:

```csv
Я бросил IT и стал фермером,18.2,35,45200,1240,4.2
Как я спал по 4 часа и ничего не понял,22.5,28,128700,3150,3.1
```

---

## Reports

### clickbait

Filters rows based on predefined criteria (e.g. high CTR and low retention).

---

## Output

Results are printed as a formatted table using `tabulate`.

Example:

```text
+----------------------------------------------+------+----------------+--------+-------+------------------+
| title                                        | ctr  | retention_rate | views  | likes | avg_watch_time   |
+----------------------------------------------+------+----------------+--------+-------+------------------+
| Я бросил IT и стал фермером                  | 18.2 | 35             | 45200  | 1240  | 4.2              |
| Секрет который скрывают тимлиды              | 25.0 | 22             | 254000 | 8900  | 2.5              |
+----------------------------------------------+------+----------------+--------+-------+------------------+
```

---

## Errors

* Only CSV files are supported
* Required columns must be present
* Missing or invalid data will raise an exception

---

## Development

Run tests:

```bash
uv run pytest
```

---

## Project Structure

```text
.
├── examples/              # sample CSV files
├── src/csv_metrics/
│   ├── presentation/      # CLI, wiring, output formatting
│   ├── application/       # use cases, interfaces, reports
│   ├── domain/            # core models (e.g. VideoMetrics)
│   └── infrastructure/    # CSV reading, mappers, repositories
├── tests/                 # unit, integration, e2e tests
└── pyproject.toml
```
