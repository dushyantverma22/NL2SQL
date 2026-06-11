import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

metadata_path = Path("metadata")

schema_embeddings = []

for file in metadata_path.glob("*.json"):

    with open(file, "r") as f:
        data = json.load(f)

    text = f"""
Table Name: {data['table_name']}

Description:
{data['description']}
"""

    # Add relationships if present
    if "relationships" in data:

        text += "\nRelationships:\n"

        for relation in data["relationships"]:
            text += f"{relation}\n"

    text += "\nColumns:\n"

    for col in data["columns"]:

        text += f"""
{col['name']}:
{col['description']}
"""

    response = client.embeddings.create(
        model="text-embedding-3-large",
        input=text
    )

    embedding = response.data[0].embedding

    schema_embeddings.append(
        {
            "table_name": data["table_name"],
            "text": text,
            "embedding": embedding
        }
    )

    print(f"✅ Embedded: {data['table_name']}")
    print(f"Dimension: {len(embedding)}")

print(
    f"\nTotal Tables Embedded: {len(schema_embeddings)}"
)