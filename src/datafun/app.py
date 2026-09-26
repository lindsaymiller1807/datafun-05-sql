"""src/datafun/app.py - Project script.

Author: Denise Case
Date: 2026-08

HOW TO RUN THIS FILE:

From the VS Code menu (with only this project open in VS Code),
click "Terminal" / New Terminal to
open an integrated Terminal in the root project folder.
Paste the following command and press ENTER or RETURN
to run this file as a script:

uv run python -m datafun.app

DOMAIN:

A library dataset with books and reviews.

The data is stored in three related CSV files:

- one row per region
- one row per store
- one row per employee

One region can have many stores.
One store can have many employees.

EXPLORE:

Sometimes the information needed for an analysis
is stored in more than one related table.

SQL is especially useful when tables share keys
and we want to analyze information across them.

A simple Python and SQL process is:

1. LOAD the related tables.
2. INSPECT the grain and keys.
3. CREATE a SQLite database.
4. LOAD the tables into SQLite.
5. QUERY across related tables with SQL.
6. VISUALIZE the query result with Python.
7. SUMMARIZE what you found.
8. DISPLAY the visualization.

DESIGN:

Use this file to declare the data-specific choices
and the reasoning behind them,
then orchestrate the work.

SQLite comes from the Python Standard Library.
Pandas loads tabular data into SQLite
and returns SQL query results as DataFrames.
Reusable visualization functions come from eda-vizkit.

The SQL stays here because the query is an
analytical decision specific to this project.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
import sqlite3
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
from eda_vizkit import save_chart
import matplotlib.pyplot as plt
import pandas as pd

# === CONFIGURE LOGGER ONCE FOR THE APPLICATION ===

LOG: logging.Logger = get_logger("P05", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

# Some global variables are CONSTANT.
# They do NOT change while the program runs.
# By convention, constants use UPPERCASE_WITH_UNDERSCORES.
# Final indicates that the value should not be reassigned.

# === LOCATE THE DATA FILES ===

DATA_DIR: Final[Path] = Path("data") / "library"

BOOK_FILE: Final[Path] = DATA_DIR / "book.csv"
REVIEW_FILE: Final[Path] = DATA_DIR / "review.csv"

# === LOCATE THE SQLITE DATABASE ===

DATABASE_FILE: Final[Path] = DATA_DIR / "library.sqlite"

# === LOCATE THE CHART OUTPUT ===

CHART_DIR: Final[Path] = Path("docs") / "images"
CHART_PATH: Final[Path] = CHART_DIR / "first-chart.png"

# === DETERMINE WHAT ONE ROW REPRESENTS ===

BOOK_GRAIN: Final[str] = "one book"
REVIEW_GRAIN: Final[str] = "one review"

# === DESCRIBE THE TABLE RELATIONSHIPS ===

RELATIONSHIP_DECISION: Final[str] = r"""
The data is stored in two related tables.

One book can have many reviews.
The reviews table uses book_id to identify the book being reviewed.

The shared book_id key connects the books and reviews tables.
"""

# === DEFINE THE ANALYTICAL QUESTION ===

CUSTOM_QUERY_DECISION: Final[str] = r"""
I want to compare the average review rating for each book genre.

The result should have one row per genre.

The information I need requires two tables:
- genre is in the books table,
- rating is in the reviews table.

The tables are connected using book_id.
"""

# === WRITE THE SQL QUERY ===

CUSTOM_SQL_QUERY: Final[str] = """
SELECT
    b.genre,
    ROUND(AVG(r.rating), 2) AS average_rating,
    COUNT(r.review_id) AS review_count
FROM books AS b
JOIN reviews AS r
    ON b.book_id = r.book_id
GROUP BY
    b.genre
ORDER BY
    average_rating DESC;
"""

# === CHOOSE A VISUALIZATION ===


# === CHOOSE A VISUALIZATION ===

CUSTOM_CHART_DECISION: Final[str] = r"""
The query result has one average rating value for each book genre.

A bar chart works well for comparing
average ratings across named genres.
"""


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Entry point when running this file as a Python script.

    This is where the instructions begin.

    Arguments: None.
    Returns: None.
    """
    log_header(LOG, "P05 - PYTHON AND SQL")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    LOG.info("-------------------------------")
    LOG.info("01. LOAD the related tables.")
    LOG.info("-------------------------------")


books_df: pd.DataFrame = pd.read_csv(BOOK_FILE)
reviews_df: pd.DataFrame = pd.read_csv(REVIEW_FILE)

LOG.info(f"Books grain: {BOOK_GRAIN}")
LOG.info(f"Reviews grain: {REVIEW_GRAIN}")

LOG.info(f"Books columns: {books_df.columns.tolist()}")
LOG.info(f"Reviews columns: {reviews_df.columns.tolist()}")

LOG.info(RELATIONSHIP_DECISION)

log_path(LOG, "books file", path=BOOK_FILE)
log_path(LOG, "reviews file", path=REVIEW_FILE)

connection: sqlite3.Connection = sqlite3.connect(DATABASE_FILE)

LOG.info("SQLite database connection created.")

LOG.info("-------------------------------")
LOG.info("04. LOAD the tables into SQLite.")
LOG.info("-------------------------------")

books_df.to_sql(
    "books",
    connection,
    if_exists="replace",
    index=False,
)

reviews_df.to_sql(
    "reviews",
    connection,
    if_exists="replace",
    index=False,
)

LOG.info("Related tables loaded into SQLite.")

LOG.info("-------------------------------")
LOG.info("05. QUERY across related tables with SQL.")
LOG.info("-------------------------------")

LOG.info(CUSTOM_QUERY_DECISION)
LOG.info(f"\nSQL query:\n{CUSTOM_SQL_QUERY}")

result_df: pd.DataFrame = pd.read_sql_query(
    CUSTOM_SQL_QUERY,
    connection,
)

LOG.info(f"\nQuery result:\n{result_df}")

LOG.info("-------------------------------")
LOG.info("06. VISUALIZE the query result with Python.")
LOG.info("-------------------------------")

LOG.info(CUSTOM_CHART_DECISION)

genre_ax = result_df.plot.bar(
    x="genre",
    y="average_rating",
    legend=False,
)

genre_ax.set_title("Average Review Rating by Genre")
genre_ax.set_xlabel("Genre")
genre_ax.set_ylabel("Average Rating")

CHART_DIR.mkdir(parents=True, exist_ok=True)

save_chart(
    genre_ax,
    CHART_PATH,
)

LOG.info(f"Chart saved successfully at {CHART_PATH}.")

LOG.info("-------------------------------")
LOG.info("07. SUMMARIZE what you found.")
LOG.info("-------------------------------")

# Run this app first.
# Review the SQL result and visualization.
# Then record your CUSTOM observations
# in a simple multi-line raw string.

LOG.info(r"""CUSTOM OBSERVATIONS:
    The SQL query connected information from
    the books and reviews tables.

    The result has one row per genre.

I observed that Mystery had the highest average review rating at 3.62,
while Fiction had the lowest average rating at 3.14.
The average ratings were fairly close across all six genres.

Based on this result, I would next like to explore whether the number
of reviews or the length of the books has any relationship with the ratings.
""")


LOG.info("================================")
LOG.info("08. DISPLAY the visualization.")
LOG.info("================================")

plt.show()

connection.close()

LOG.info("================================")
LOG.info("END main() - Executed successfully!")
LOG.info("================================")

# === CONDITIONAL EXECUTION GUARD ===

# WHY: This is standard Python "boilerplate" - we copy and paste it
# into every Python script. It is a "conditional execution" guard,
# meaning: if this file is being run as a script, then execute the code
# in the main() function.

if __name__ == "__main__":
    main()
