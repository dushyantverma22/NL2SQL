from validation.sql_validator import validate_sql

sql = """
SELECT *
FROM customers
"""

print(validate_sql(sql))