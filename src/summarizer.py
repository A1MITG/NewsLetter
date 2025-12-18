import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text, prompt=None):
    if not prompt:
        prompt = (
            "Summarize the following news article for a CXO audience in 2-3 sentences, "
            "focusing on executive impact, decisions, and key actions. Output in plain text."
        )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],
        max_tokens=200,
        temperature=0.5
    )
    return response.choices[0].message["content"].strip()
