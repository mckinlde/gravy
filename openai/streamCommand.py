import os
import openai

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a chat completion
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Print the assistant's reply
print(response.choices[0].message.content)  # Correct property access
