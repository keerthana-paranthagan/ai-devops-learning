import requests
import json

url = "http://localhost:11434/api/generate"

prompt = """
Answer only in JSON.

Question:
What is Terraform?

Format:
{
  "tool": "",
  "purpose": ""
}
"""

payload = {
    "model": "llama3.2:1b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(
    url,
    json=payload
)

result = response.json()["response"]

print(result)

data = json.loads(result)

print(data["tool"])
print(data["purpose"])