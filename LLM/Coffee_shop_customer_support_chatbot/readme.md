# ☕ Nikunja Abir’s Cafe – Local LLM RAG Chatbot 🇧🇩

A fully local AI-powered coffee shop chatbot built using 4-bit quantized Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).  
The system runs offline using open-source models and answers customer questions based on real cafe data.

---

## Project Overview

This project implements an intelligent assistant (BrewBot) for Nikunja Abir’s Cafe.  
It can answer questions about menu items, prices, daily specials, opening hours, allergies, and cafe facilities by retrieving relevant documents and generating grounded responses.

---

## RAG Architecture

User Query  
→ Vector Similarity Search (ChromaDB)  
→ Relevant Cafe Documents  
→ Context Injection into Prompt  
→ 4-bit Quantized LLM (Phi-2)  
→ Final Response  

---

## Technology Stack

- Language Model: Microsoft Phi-2 (2.7B)
- Quantization: bitsandbytes (4-bit NF4)
- Framework: HuggingFace Transformers
- RAG Pipeline: LangChain
- Embeddings: all-MiniLM-L6-v2
- Vector Database: ChromaDB
- Hardware: NVIDIA GPU (CUDA)

---

## Project Structure

coffee-shop-rag/
- data/
  - menu.json
  - specials.json
  - coffee_shop_info.txt
- vector_db/
  - chroma.sqlite3
- notebook.ipynb
- README.md

---

## Knowledge Sources

- Cafe profile and owner information
- Menu items and prices
- Daily specials and discounts
- Operating hours
- Allergy and dietary information
- Facilities and services

All responses are generated strictly from these sources.

---

## Example Questions

- What coffee drinks do you have?
- How much is a cappuccino?
- Do you have any specials today?
- Is lactose-free milk available?
- What time do you open on Friday?

---

## Key Features

- Fully local execution
- No paid or cloud APIs
- Low VRAM usage with 4-bit quantization
- GPU acceleration
- Conversational memory
- Real Bangladeshi cafe use case

---

## Author

Abir Rauf  
Owner, Nikunja Abir’s Cafe  
Dhaka, Bangladesh

---

## License

For educational and research purposes only.  
Free to modify and extend for personal or academic use.

