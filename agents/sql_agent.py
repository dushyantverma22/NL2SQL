import os

from dotenv import load_dotenv
from openai import OpenAI

from rag.schema_retriever import (
    get_schema_context
)

from prompts.sql_prompt import (
    build_sql_prompt
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_sql(question: str):

    schema_context = get_schema_context(
        question
    )

    prompt = build_sql_prompt(
        question,
        schema_context
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
    "role": "system",
    "content": """
You are a PostgreSQL SQL expert.

Rules:
1. Return only SQL.
2. Do not return markdown.
3. Do not explain the query.
4. Do not use tables or columns not present in schema.
5. Output must be executable PostgreSQL SQL.
"""
},
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    sql = (
        response
        .choices[0]
        .message
        .content
    )

    # Remove markdown formatting
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql


if __name__ == "__main__":

    question = (
        "Top 10 customers by revenue in Delhi"
    )

    sql = generate_sql(question)

    print("\nGenerated SQL:\n")

    print(sql)