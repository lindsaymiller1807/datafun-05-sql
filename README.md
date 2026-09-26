# datafun-05-sql

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![marimo](https://img.shields.io/badge/marimo-reactive_notebook-FF6B6B)](https://docs.marimo.io/)
[![SQLite](https://img.shields.io/badge/SQLite-database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python and SQL project analyzing library book review data.
> This project compares average review ratings across book genres using related tables.

This project uses Python, pandas, SQLite, and SQL to analyze related library data.
The books and reviews tables are connected using `book_id`.

The analysis calculates the average review rating for each genre and displays the
results in a bar chart.

## Motivation

We've mostly worked with data stored in files.
Organizations often keep larger collections of related data in databases,
where we can ask for the information we need
instead of loading everything at once.

In this project, we'll use SQL to ask questions of data stored in a database.
We'll select useful records, filter and organize results,
summarize groups, and combine related information
so it can be used in further analysis.

## This Project

This project uses **relational data, SQLite, SQL, Python, and pandas**
to analyze library book review data.

The analysis uses two related tables:

- **books** — contains book information such as title, genre, branch, and pages
- **reviews** — contains review ratings linked to books using `book_id`

The project asks:

**How does the average review rating compare across book genres?**

SQL joins the books and reviews tables, groups the results by genre,
and calculates the average rating for each genre.

The results are then visualized with Python using a bar chart.



## Produced Artifacts

This project produces several useful outputs:

- **Genre Rating Chart** — `docs/images/first-chart.png`
- **SQLite database** — generated from the library CSV files
- **Project log** — records the steps and results from each program run

## Library Genre Rating Analysis

![Average Review Rating by Genre](docs/images/first-chart.png)

This analysis compares the average review rating across six book genres using data from the books and reviews tables.

Mystery had the highest average rating at 3.62, while Fiction had the lowest at 3.14. Overall, the average ratings were fairly close across all six genres.

## Important Folders and Files

- **data/library/** - library CSV input files and generated SQLite database
- **docs/** - project narrative and documentation
- **docs/images/** - generated chart images
- **src/datafun/** - Python project logic
- **project.log** - records program execution and results
- **zensical.toml** - documentation site configuration

## How to Run

From the root project folder, run:

```bash
uv run python -m datafun.app
```

## Skills Demonstrated

This project demonstrates experience with:

- Python
- pandas
- SQL
- SQLite
- relational data
- joining related tables
- grouping and aggregating data
- data visualization
- Git and GitHub
- GitHub Actions
- project documentation

## License

This project is licensed under the [MIT License](./LICENSE).
