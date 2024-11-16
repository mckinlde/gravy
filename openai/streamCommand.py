import os
import openai

# You can find your api key at: https://platform.openai.com/api-keys
# to set it, copy/paste into :$ export OPENAI_API_KEY=""
openai.api_key = os.getenv("OPENAI_API_KEY")

# gets API Key from environment variable OPENAI_API_KEY
client = openai.OpenAI()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, how are you?"}]
)
print(response['choices'][0]['message']['content'])
