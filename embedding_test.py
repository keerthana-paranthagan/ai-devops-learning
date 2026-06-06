import requests

url = "http://localhost:11434/api/embeddings"

payload = {
    "model": "nomic-embed-text",
    "prompt": "K8s"
}

response = requests.post(url, json=payload)

data = response.json()

print(data)