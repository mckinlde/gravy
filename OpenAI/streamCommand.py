import os
import openai
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is set
if openai.api_key is None:
    raise ValueError("API key is missing. Please set the OPENAI_API_KEY in your .env file.")

# Create a chat completion
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Print the assistant's reply
print(response['choices'][0]['message']['content'])  # Correct property access
