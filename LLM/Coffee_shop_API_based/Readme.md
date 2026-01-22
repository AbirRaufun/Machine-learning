# Gemini Coffee Shop RAG System - Fixed Version

A complete, working implementation of a Retrieval-Augmented Generation (RAG) system using Google's Gemini API and ChromaDB vector database for a coffee shop assistant.

## 🚀 Features

- **Gemini API Integration**: Uses `gemini-3-flash-preview` model
- **Vector Database**: ChromaDB with persistent storage
- **Chat History**: Maintains conversation context
- **Error Handling**: Comprehensive error handling and fallbacks
- **Source Attribution**: Shows which documents were used for answers
- **Interactive Chat**: Command-line interface for testing

## 📁 File Structure
gemini_rag_fixed.py
├── GeminiCoffeeRAG class
│ ├── init() - Initialize API and vector DB
│ ├── retrieve_context() - Query vector database
│ ├── format_prompt() - Build prompt with context
│ ├── generate_response() - Generate answers
│ ├── clear_history() - Clear chat memory
│ └── test_system() - Run test queries
└── Main execution block

## 🔧 Installation Requirements

```bash
pip install google-generativeai chromadb

# Gemini Coffee Shop RAG - README

This is a fixed version of the Gemini RAG system for a coffee shop assistant.

## How to Use

1. **Add your Gemini API key** in the `API_KEY` variable
2. **Ensure your vector database** is in the `./vector_db` folder
3. **Run the script**: `python gemini_rag_fixed.py`

## Commands
- Type your question to chat
- Type `clear` to reset chat history  
- Type `exit`, `quit`, or `bye` to end



