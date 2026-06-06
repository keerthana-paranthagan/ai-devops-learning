import requests

EMBED_URL = "http://localhost:11434/api/embeddings"

documents = []

with open("company_docs.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            documents.append(line)

def get_embedding(text):
    payload = {
        "model": "nomic-embed-text",
        "prompt": text
    }

    response = requests.post(
        EMBED_URL,
        json=payload
    )

    return response.json()["embedding"]

def cosine_similarity(a, b):
    dot = sum(x*y for x, y in zip(a, b))

    norm_a = sum(x*x for x in a) ** 0.5
    norm_b = sum(x*x for x in b) ** 0.5

    return dot / (norm_a * norm_b)

document_embeddings = []

print("Creating embeddings...")

for doc in documents:
    embedding = get_embedding(doc)

    document_embeddings.append({
        "text": doc,
        "embedding": embedding
    })

print("Ready!")

question = input("Ask a question: ")

question_embedding = get_embedding(question)

best_match = None
best_score = -1

for doc in document_embeddings:

    score = cosine_similarity(
        question_embedding,
        doc["embedding"]
    )

    if score > best_score:
        best_score = score
        best_match = doc["text"]

print("\nMost Relevant Document:")
print(best_match)




# Document
# ↓
# Embedding
# ↓
# Storage

# Question
# ↓
# Embedding
# ↓
# Similarity Search
# ↓
# Relevant Result