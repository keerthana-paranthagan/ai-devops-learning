import requests

url = "http://localhost:11434/api/generate"

while True:
    question = input("Ask something: ")

    if question.lower() == "exit":
        break

    payload = {
        "model": "llama3.2:1b",
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, json=payload)

    answer = response.json()["response"]

    print("\nAI:", answer)
    print()