# 📄 RAG PDF Chat Application

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content using AI. The application extracts text from PDFs, generates vector embeddings, stores them in Qdrant, retrieves the most relevant document chunks, and uses an OpenAI language model to generate context-aware responses.

---

## 🚀 Features

* Upload and process PDF documents
* Automatic text extraction and chunking
* Generate embeddings using OpenAI Embeddings
* Store embeddings in Qdrant Vector Database
* Semantic similarity search
* AI-powered question answering using Retrieval-Augmented Generation (RAG)
* Interactive Streamlit web interface

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **OpenAI API**
* **Qdrant Vector Database**
* **LangChain**
* **Inngest**
* **PyPDF**

---

## 📁 Project Structure

```text
Rag/
│
├── app/
│   ├── ingestion/
│   ├── rag/
│   ├── storage/
│   ├── embeddings/
│   └── utils/
│
├── streamlit_app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rag-pdf-chat.git
cd rag-pdf-chat
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Start Qdrant

Run Qdrant locally using Docker:

```bash
docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add the following:

```env
OPENAI_API_KEY=your_openai_api_key

QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION=pdf_documents

INNGEST_EVENT_KEY=your_event_key
INNGEST_SIGNING_KEY=your_signing_key
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

## 📖 How It Works

1. Upload a PDF document.
2. The application extracts text from the document.
3. The text is split into smaller chunks.
4. Embeddings are generated for each chunk.
5. The embeddings are stored in Qdrant.
6. When a user asks a question:

   * The question is converted into an embedding.
   * Relevant document chunks are retrieved using semantic search.
   * The retrieved context is passed to the language model.
   * The AI generates an accurate, context-aware answer.

---

## 🔄 Workflow

```text
          PDF Upload
               │
               ▼
      Text Extraction
               │
               ▼
      Document Chunking
               │
               ▼
   Embedding Generation
               │
               ▼
      Store in Qdrant
               │
               ▼
        User Question
               │
               ▼
    Semantic Vector Search
               │
               ▼
 Retrieve Relevant Chunks
               │
               ▼
      OpenAI Language Model
               │
               ▼
         Generated Answer
```

---

## 💡 Example Questions

* Summarize this document.
* What are the key findings?
* Explain the main concepts.
* What conclusions are presented?
* Compare two sections of the document.

---

## 📌 Future Improvements

* Support multiple document uploads
* Conversation history
* Hybrid keyword and vector search
* Highlight source passages
* Streaming AI responses
* Support for DOCX and TXT files
* User authentication

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shaikh Tohid**

If you found this project useful, consider giving it a ⭐ on GitHub.
