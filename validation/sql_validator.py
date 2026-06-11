import sqlglot


FORBIDDEN_KEYWORDS = [
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "TRUNCATE",
    "ALTER",
    "CREATE"
]


def validate_sql(sql: str):
    """
    Validate SQL syntax and block dangerous operations.
    """

    try:
        sqlglot.parse_one(sql)

    except Exception as e:
        return False, f"SQL Syntax Error: {e}"

    upper_sql = sql.upper()

    for keyword in FORBIDDEN_KEYWORDS:

        if keyword in upper_sql:
            return (
                False,
                f"Forbidden operation detected: {keyword}"
            )

    return True, "SQL Valid"