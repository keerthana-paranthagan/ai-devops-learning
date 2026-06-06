import requests

url = "http://localhost:11434/api/generate"

conversation_history = ""

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    conversation_history += f"\nUser: {user_input}"

    payload = {
        "model": "llama3.2:1b",
        "prompt": conversation_history,
        "stream": False
    }

    response = requests.post(url, json=payload)

    ai_response = response.json()["response"]

    print("\nAI:", ai_response)
    print()

    conversation_history += f"\nAI: {ai_response}"