import random

questions = [
    "Explain Spark execution architecture.",
    "How do you troubleshoot slow Azure Databricks jobs?",
    "Explain Delta Lake transaction log.",
    "Design a near real-time ingestion pipeline.",
    "How do you detect and fix data skew?",
    "Explain OPTIMIZE, ZORDER and VACUUM in Delta Lake.",
]

def get_question():
    return random.choice(questions)