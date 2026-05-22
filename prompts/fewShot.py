## the model is given a direct question with few examples is few-shot prompting in AI.
## IT USED MORE REAL WORLD

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

Examples: 
Question : Can you explain the a + b whole square?
Answer : Sorry, I can only help with Coding related questions.

Question : Hey, write a code in python for adding two numbers.
Answer : def add(a, b):
            return a + b

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
            "content" : "what is earth?"
         }
    ]
)

print(response.choices[0].message.content)