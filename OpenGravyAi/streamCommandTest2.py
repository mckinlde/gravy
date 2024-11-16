from openai import OpenAI
client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
)

def get_response(prompt):
    if prompt:
        print(f"prompt: {prompt}")
    else:
        prompt = "Give me a python function that find costumes for cats"

    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{prompt}, please only return the python code that will be copy/pasted and run."}]
    )

    print(chat_completion)
    return chat_completion

#export OPENAI_API_KEY=""