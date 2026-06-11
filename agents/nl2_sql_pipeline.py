import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from agents.sql_agent import generate_sql

from validation.sql_validator import (
    validate_sql
)

from validation.schema_validator import (
    validate_tables
)

from execution.query_executor import (
    execute_query
)

from agents.insight_agent import (
    generate_insight
)


def run_pipeline(question: str):

    print("\n" + "=" * 60)
    print("QUESTION")
    print("=" * 60)
    print(question)

    # ------------------------------------------------
    # Generate SQL
    # ------------------------------------------------

    sql = generate_sql(question)

    print("\n" + "=" * 60)
    print("GENERATED SQL")
    print("=" * 60)
    print(sql)

    # ------------------------------------------------
    # Validate SQL
    # ------------------------------------------------

    valid, msg = validate_sql(sql)

    if not valid:
        raise Exception(msg)

    print("\n✅ SQL Validation Passed")

    # ------------------------------------------------
    # Validate Tables
    # ------------------------------------------------

    valid, msg = validate_tables(sql)

    if not valid:
        raise Exception(msg)

    print("✅ Schema Validation Passed")

    # ------------------------------------------------
    # Execute Query
    # ------------------------------------------------

    columns, rows = execute_query(sql)

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)

    print(columns)

    for row in rows[:10]:
        print(row)

    insight = generate_insight(
    question,
    columns,
    rows
)

    print("\n")
    print("="*60)
    print("BUSINESS INSIGHTS")
    print("="*60)

    print(insight)

    return columns, rows



if __name__ == "__main__":

    question = (
        "Top 10 customers by revenue in Delhi"
    )

    run_pipeline(question)