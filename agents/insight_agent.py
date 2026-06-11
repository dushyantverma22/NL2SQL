import os
import pandas as pd

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_insight(
        question,
        columns,
        rows
):

    df = pd.DataFrame(
        rows,
        columns=columns
    )

    data_preview = df.head(20).to_string()

    prompt = f"""
Question:
{question}

Results:
{data_preview}

Generate concise business insights.

Include:
1. Key findings
2. Trends
3. Important observations

Keep under 150 words.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return (
        response
        .choices[0]
        .message
        .content
    )