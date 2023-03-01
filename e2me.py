#!/usr/bin/env python
import sys
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API credentials
openai.api_key = os.getenv("CGPT_API_KEY")

# Define your prompt
print(sys.argv[1])
prompt = "For the command below - 1.tell me if it is valid command or not - 2.If not valid explain the error. - 3. If valid describes what will be executed \n\n" + sys.argv[1]

# Set up request parameters
model_engine = "text-davinci-002"
temperature = 0.7
max_tokens = 50

# Send request to OpenAI API
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
)

# Extract the generated text from the response
generated_text = response.choices[0].text

# Print the generated text
print(generated_text)