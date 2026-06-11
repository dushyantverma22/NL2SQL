import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv()

# ----------------------------
# Clients
# ----------------------------

openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index(
    os.getenv("PINECONE_INDEX")
)

# ----------------------------
# Metadata Folder
# ----------------------------

metadata_path = Path("metadata")

vectors = []

for file in metadata_path.glob("*.json"):

    with open(file, "r") as f:
        data = json.load(f)

    text = f"""
Table Name: {data['table_name']}

Description:
{data['description']}
"""
    if "business_terms" in data:
        text += "\nBusiness Terms:\n"

        for term in data["business_terms"]:
            text += term + "\n"

    if "relationships" in data:

        text += "\nRelationships:\n"

        for relation in data["relationships"]:
            text += relation + "\n"

    text += "\nColumns:\n"

    for col in data["columns"]:

        text += (
            f"{col['name']}: "
            f"{col['description']}\n"
        )

    response = openai_client.embeddings.create(
        model="text-embedding-3-large",
        input=text
    )

    embedding = response.data[0].embedding

    vectors.append(
        {
            "id": data["table_name"],
            "values": embedding,
            "metadata": {
                "table_name": data["table_name"],
                "schema_text": text
            }
        }
    )

# ----------------------------
# Upload to Pinecone
# ----------------------------

index.upsert(vectors=vectors)

print(
    f"✅ Uploaded {len(vectors)} tables to Pinecone"
)