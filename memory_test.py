import requests

url = "http://localhost:11434/api/generate"

prompt = "My name is Keerthi.I work as a DevOps Engineer.What is my profession?."

payload = {
    "model": "llama3.2:1b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=payload)

print(response.json()["response"])