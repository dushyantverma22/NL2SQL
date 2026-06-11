import os

from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index(
    os.getenv("PINECONE_INDEX")
)


def retrieve_schema(
    question: str,
    top_k: int = 3
):

    response = openai_client.embeddings.create(
        model="text-embedding-3-large",
        input=question
    )

    query_embedding = response.data[0].embedding

    result = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    return result


def get_schema_context(
    question: str,
    top_k: int = 3
):

    result = retrieve_schema(
        question,
        top_k
    )

    schema_texts = []

    for match in result["matches"]:

        schema_texts.append(
            match["metadata"]["schema_text"]
        )

    return "\n\n".join(schema_texts)


if __name__ == "__main__":

    question = (
        "Payment success rate"
    )

    result = retrieve_schema(question)

    print("\nRetrieved Tables:\n")

    for match in result["matches"]:

        print(
            match["metadata"]["table_name"],
            round(match["score"], 4)
        )

