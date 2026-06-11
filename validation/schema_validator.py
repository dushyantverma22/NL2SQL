import re


VALID_TABLES = {
    "customers",
    "products",
    "orders",
    "payments",
    "query_logs"
}


def validate_tables(sql: str):
    """
    Extract tables from SQL and verify they exist.
    """

    matches = re.findall(
        r"FROM\s+(\w+)|JOIN\s+(\w+)",
        sql,
        flags=re.IGNORECASE
    )

    tables = set()

    for match in matches:

        for table in match:

            if table:
                tables.add(table.lower())

    invalid_tables = tables - VALID_TABLES

    if invalid_tables:

        return (
            False,
            f"Invalid tables detected: {invalid_tables}"
        )

    return True, "Tables Valid"