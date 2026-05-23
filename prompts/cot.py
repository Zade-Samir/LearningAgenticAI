# Chain Of Thought Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os

import json

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10  = 1.5" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
    OUTPUT: { "step": "OUTPUT": "content": "3.5" }
"""


response = client.chat.completions.create(
    model = "gemini-2.5-flash",
    response_format = {"type" : "json_object"},
    messages = [
        {
            "role" : "system",
            "content" : SYSTEM_PROMPT
         },
        {
            "role" : "user",
            "content" : "Hey, write code to add two numbers in python"
         },
         ## manually adding the history for keep the assistant
         {
             "role" : "assistant",
             "content" : json.dumps(
                {
                    "step": "PLAN",
                    "content": "The user wants Python code to add two numbers. I should provide a simple function that takes two arguments, adds them, and returns the result. I will also include an example of how to call the function."
                }
             )
         }

         ##output got directly
         
        #  {
        # "step": "OUTPUT",
        # "content": "```python\ndef add_two_numbers(num1, num2):\n    \"\"\"This function takes two numbers as input and returns their sum.\n    \"\"\"\n    return num1 + num2\n\n# Example usage:\nnumber1 = 5\nnumber2 = 10\n\nsum_result = add_two_numbers(number1, number2)\nprint(f\"The sum of {number1} and {number2} is: {sum_result}\")\n\n# Another example:\nprint(f\"The sum of 7 and 3 is: {add_two_numbers(7, 3)}\")\n```"
        # } 
        
    ]
)

print(response.choices[0].message.content)