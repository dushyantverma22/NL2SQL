def build_sql_prompt(
    question: str,
    schema_context: str
) -> str:

    prompt = f"""
You are an expert PostgreSQL SQL developer.

Generate a valid PostgreSQL query.

Rules:
1. Use only tables and columns provided.
2. Do not invent columns.
3. Return only SQL.
4. Use proper joins.
5. Limit results when appropriate.

Schema:

{schema_context}

Question:

{question}

SQL:
"""

    return prompt