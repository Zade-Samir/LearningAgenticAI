## the model is given a direct question or task without prior examples is zero-shot prompting in AI.
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You should only and only answer the coding related questions. Do not answer anything else. You're name is AlexaBai. If user asks something other than coding, just say sorry.
"""

response = client.chat.completions.create(
    model = "gemini-2.5-flash",
    messages = [
        {
            "role" : "system",
            "content" : SYSTEM_PROMPT
         },
        {
            "role" : "user",
            "content" : "can we make main class as final in java?"
         }
    ]
)

print(response.choices[0].message.content)