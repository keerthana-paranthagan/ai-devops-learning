import requests
import json

url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.2:1b",
    "prompt": "Explain Docker in one sentence.",
    "stream": False
}

response = requests.post(url, json=payload)

data = response.json()

print(data["response"])