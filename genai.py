import os
import sys
from dotenv import load_dotenv
import traceback

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types


system_prompt = """
No matter what I type, say `Hello there!` first. 
"""

user_prompt = sys.argv[1]


messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]


client = genai.Client(api_key=api_key)


response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
    )
)

candidates = response.candidates
