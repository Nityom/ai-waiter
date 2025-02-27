import json
import faiss
import numpy as np
import ollama
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load menu data
with open("menu.json", "r") as f:
    menu = json.load(f)

# Use LLaMA via Ollama to generate embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Convert menu descriptions into vector embeddings
texts = [item["description"] for item in menu]
vectors = embedding_model.embed_documents(texts)

# Convert to FAISS format
dimension = len(vectors[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(vectors, dtype=np.float32))

# Save FAISS index
faiss.write_index(index, "menu_index.faiss")
print("FAISS index created and saved.")
