# 🎙 Audio-to-Text RAG for Podcast Search

## 📌 Overview
This project is an **Audio-to-Text Retrieval-Augmented Generation (RAG) system** that allows users to **search podcasts with timestamps**.  
Given an audio file (e.g., a podcast episode), it:
1. Converts speech to text
2. Stores transcripts in a database with embeddings
3. Lets users **search for any query** and instantly find the exact segment & timestamp in the podcast.

The **frontend** is built with **Streamlit**, the backend uses **ChromaDB** for storing embeddings, and **Sentence Transformers** for semantic search.

---

## 🚀 Features
- 🎧 **Audio transcription** using OpenAI Whisper  
- 🔍 **Semantic search** across transcripts  
- ⏱ **Timestamps** for precise navigation  
- 🗂 **ChromaDB index** for storing embeddings  
- 🌐 **Streamlit UI** for easy interaction  
- ☁ **Deployed on Hugging Face Spaces**

---

## 🛠 Tech Stack
- **Python**  
- **OpenAI Whisper** – Audio transcription  
- **Sentence Transformers (all-MiniLM-L6-v2)** – Embedding generation  
- **ChromaDB** – Vector database  
- **Streamlit** – Frontend interface  
- **Hugging Face Spaces** – Deployment  

---

## 📂 Project Structure

podcast_rag/
│
├── app.py # Streamlit UI
├── process_audio.py # Audio processing & transcription
├── build_index.py # Create embeddings index
├── query_engine.py # Query ChromaDB
├── requirements.txt # Dependencies
│
├── transcripts/ # JSON transcripts
├── index/ # ChromaDB index files
├── cleaned.wav # Processed audio file
├── README.md # Documentation
