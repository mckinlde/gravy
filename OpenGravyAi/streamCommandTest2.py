from openai import OpenAI
client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
)

prompt = "Give me a python function that find costumes for cats"

chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Give me a python function that find costumes for cats"}]
)



print(chat_completion)