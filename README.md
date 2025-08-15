🎙 Audio-to-Text RAG for Podcast Search
📌 Overview

This project is an Audio-to-Text Retrieval-Augmented Generation (RAG) system that allows users to search podcasts with timestamps.
Given an audio file (e.g., a podcast episode), it:

Converts speech to text

Stores transcripts in a database with embeddings

Lets users search for any query and instantly find the exact segment & timestamp in the podcast.

The frontend is built with Streamlit, the backend uses ChromaDB for storing embeddings, and Sentence Transformers for semantic search.

🚀 Features

🎧 Audio transcription using OpenAI Whisper

🔍 Semantic search across transcripts

⏱ Timestamps for precise navigation

🗂 ChromaDB index for storing embeddings

🌐 Streamlit UI for easy interaction

☁ Deployed on Hugging Face Spaces

🛠 Tech Stack

Python

OpenAI Whisper – Audio transcription

Sentence Transformers (all-MiniLM-L6-v2) – Embedding generation

ChromaDB – Vector database

Streamlit – Frontend interface

Hugging Face Spaces – Deployment

📂 Project Structure
podcast_rag/
│
├── app.py                 # Streamlit UI
├── process_audio.py       # Audio processing & transcription
├── build_index.py         # Create embeddings index
├── query_engine.py        # Query ChromaDB
├── requirements.txt       # Dependencies
│
├── transcripts/           # JSON transcripts
├── index/                 # ChromaDB index files
├── cleaned.wav            # Processed audio file
├── README.md              # Documentation
└── ...

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/AmitKumar-24/Audio-to-Text-RAG-for-Podcast-Search.git
cd Audio-to-Text-RAG-for-Podcast-Search

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Process the Audio & Generate Transcript
python process_audio.py


This will:

Upload audio file

Convert it to text

Save transcript in transcripts/

4️⃣ Build the ChromaDB Index
python build_index.py

5️⃣ Run the Streamlit App (Locally)
streamlit run app.py

🌐 Deployment on Hugging Face Spaces
Step 1 – Create a Space

Go to Hugging Face Spaces

Click Create New Space

Fill details:

Name: podcast-search-rag

Visibility: Public

SDK: Streamlit

Step 2 – Link GitHub Repo

Go to Settings → Repository → Link to external repo

Connect to your GitHub repository

Step 3 – Upload Required Files

Ensure transcripts/ and index/ folders are uploaded

app.py should be the main file

Step 4 – Add Hugging Face Space Config in README
---
title: Podcast Search with Timestamps
emoji: 🎙
colorFrom: pink
colorTo: indigo
sdk: streamlit
sdk_version: "1.35.0"
app_file: app.py
pinned: false
---

Step 5 – Commit & Deploy

Commit the changes

Hugging Face will automatically build & host your app

Public link will be available after successful build

📷 Example Output

Query: machine learning

Results:

Text: I think that's something that I'm still trying to learn because
⏱ Timestamp: 78.6s - 84.0s (Episode: transcript1.json)

Text: What do you do?
⏱ Timestamp: 91.58s - 92.24s (Episode: transcript1.json)

📌 Future Improvements

🎯 Multi-podcast search

📁 Automatic audio file upload via UI

🎙 Direct audio playback at timestamp

🔗 Integration with YouTube podcasts

📜 License

This project is licensed under the Apache 2.0 License.
