import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

st.title("🎙 Podcast Search with Timestamps")

query = st.text_input("Ask your question:")
if query:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path="index")
    collection = client.get_collection("podcasts")

    results = collection.query(
        query_embeddings=[model.encode(query).tolist()],
        n_results=5
    )

    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        st.write(f"**Text:** {doc}")
        st.write(f"⏱ Timestamp: {meta['start']}s - {meta['end']}s (Episode: {meta['episode']})")
