# LearnMate AI 🎓

An AI-powered study assistant that helps students interact with their learning materials efficiently using Retrieval-Augmented Generation (RAG).

## 📖 Overview

Modern students rely on multiple study resources such as lecture notes, textbooks, PDFs, and research papers. These documents are often long and difficult to navigate, making it time-consuming to find specific information.

**LearnMate AI** solves this by allowing students to chat with their study materials. Instead of manually searching through pages of content, students can simply ask questions and receive accurate answers extracted directly from their documents.

By leveraging **Retrieval-Augmented Generation (RAG)**, LearnMate AI combines document retrieval with large language models to provide context-aware explanations, summaries, and answers from your own study resources.

## ✨ Features

- 📄 **PDF Support**: Load and process PDF documents automatically
- 🔍 **Smart Retrieval**: Uses MMR (Maximal Marginal Relevance) search for better context retrieval  
- 🤖 **AI-Powered Responses**: Leverages Mistral AI for intelligent answers
- 💾 **Vector Database**: Persistent storage with Chroma for fast document embedding and retrieval
- 🌐 **Interactive Chat**: Command-line interface to query your documents

## 🛠️ Tech Stack

- **LLM**: Mistral AI (mistral-small-latest)
- **Embeddings**: Mistral Embeddings (mistral-embed)
- **Vector Database**: Chroma
- **Framework**: LangChain
- **PDF Processing**: PyPDF, LangChain Community
- **Web Scraping**: BeautifulSoup4
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.8 or higher
- Mistral AI API key
- `.env` file with `MISTRAL_API_KEY`

## 🚀 Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**
   - Create a `.env` file in the project root:
   ```
   MISTRAL_API_KEY=your_api_key_here
   ```

## 📚 Project Structure

```
LearnMate AI/
├── main.py              # Interactive RAG chat interface
├── create_db.py         # Database initialization script
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .env                 # Environment variables
├── chroma_db/           # Vector database storage
└── document/
    ├── page.py          # Web content loader utility
    └── doc.txt          # Sample documents
```

## 🎯 Usage

### 1. Initialize the Vector Database

Populate the Chroma database with your documents:

```bash
python create_db.py
```

This script:
- Loads PDFs from the `document/` folder
- Splits documents into chunks (1000 characters with 200 character overlap)
- Creates embeddings using Mistral
- Stores embeddings in Chroma database

### 2. Chat with Your Documents

Start the interactive RAG system:

```bash
python main.py
```

Then:
- Enter your questions at the prompt
- The system retrieves relevant context and generates answers
- Type `0` to exit

## 🔧 Configuration

### Retrieval Settings (in main.py)
- **Search Type**: MMR (Maximal Marginal Relevance)
- **Retrieved Documents**: 4 most relevant chunks
- **Fetch Size**: 10 candidates
- **Lambda Multiplier**: 0.5 (balances relevance vs. diversity)

### Chunking Settings (in create_db.py)
- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters

## ⚠️ Limitations

- Answers are limited to content from provided documents
- If information isn't in your documents, the system will indicate that
- Quality depends on document relevance and chunking strategy

## 📄 License

Educational use project
```

Then:
- Enter your questions at the prompt
- The system retrieves relevant context and generates answers
- Type `0` to exit

### 3. Load Web Content (Optional)

Use `document/page.py` to load content from web pages:

```bash
python document/page.py
```

## 🔧 How It Works

1. **Document Ingestion**: PDFs are loaded and split into manageable chunks
2. **Embedding**: Text chunks are converted to embeddings using Mistral Embeddings
3. **Storage**: Embeddings are stored in Chroma for fast retrieval
4. **Query Processing**: User questions are embedded and matched against stored documents
5. **Answer Generation**: Relevant context is passed to Mistral LLM with system prompts
6. **Response**: AI generates contextual answers based only on your documents

### Retrieval Strategy

- **Search Type**: MMR (Maximal Marginal Relevance)
- **Retrieved Documents**: 4 most relevant chunks
- **Fetch Size**: 10 candidates (for better diversity)
- **Lambda Multiplier**: 0.5 (balances relevance vs. diversity)

## 📝 Configuration

Edit `main.py` to customize:
- **LLM Model**: Change from `mistral-small-latest` to other Mistral models
- **Embedding Model**: Use different embedding models
- **Retrieval Parameters**: Adjust `k`, `fetch_k`, and `lambda_mult` in the retriever
- **Chunk Size**: Modify chunk_size and chunk_overlap in `create_db.py`

## ⚠️ Limitations

- Answers are limited to the context from provided documents
- If information isn't in your documents, the system will indicate that
- Quality depends on document relevance and chunking strategy

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new document loaders
- Improve retrieval strategies
- Enhance the UI
- Add Streamlit web interface

## 📄 License

This project is open source and available for educational use.

## 📧 Support

For issues or questions, please refer to:
- [LangChain Documentation](https://python.langchain.com/)
- [Mistral AI Documentation](https://docs.mistral.ai/)
- [Chroma Documentation](https://docs.trychroma.com/)

---

**Happy Learning! 🚀**