from openai import OpenAI
import os

client = OpenAI()

def evaluate(question, answer):

    prompt = f"""
You are a Senior Azure Data Engineering interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Provide:
Score out of 10
What was good
What was missing
How to improve
"""

    response = client.responses.create(
        model=os.getenv("MODEL"),
        input=prompt
    )

    return response.output_text