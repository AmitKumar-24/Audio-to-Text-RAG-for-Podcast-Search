import json, os
from sentence_transformers import SentenceTransformer
import chromadb

def build_index(transcript_folder, index_folder):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path=index_folder)

    try:
        collection = client.create_collection(name="podcasts")
    except:
        collection = client.get_collection(name="podcasts")

    for file in os.listdir(transcript_folder):
        full_path = os.path.join(transcript_folder, file)
        if os.path.isdir(full_path) or not file.endswith(".json"):
            continue
        if os.path.getsize(full_path) == 0:
            print(f"Skipping empty file: {file}")
            continue

        try:
            with open(full_path) as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON: {file}")
            continue

        for seg in data.get("segments", []):
            embedding = model.encode(seg["text"]).tolist()
            collection.add(
                documents=[seg["text"]],
                embeddings=[embedding],
                metadatas=[{
                    "start": seg["start"],
                    "end": seg["end"],
                    "episode": file
                }],
                ids=[f"{file}_{seg['start']}"]
            )
    print("Index built successfully!")

if __name__ == "__main__":
    build_index("transcripts", "index")
