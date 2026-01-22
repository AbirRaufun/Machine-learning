# gemini_rag_fixed.py - COMPLETE FIXED VERSION
import google.generativeai as genai
import chromadb
from typing import List, Tuple, Dict, Any
import os
# Fixes the ChromaDB "Failed to send telemetry" error
os.environ['CHROMA_TELEMETRY'] = 'False'

class GeminiCoffeeRAG:
    def __init__(self, api_key: str, vector_db_path: str = "./vector_db"):
        """
        Initialize Gemini API with your vector database
        """
        print("🤖 Initializing Gemini Coffee Shop RAG...")
        
        # -------------------------------------------------
        # 1. SETUP GEMINI API
        # -------------------------------------------------
        print("🔧 Configuring Gemini API...")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-3-flash-preview')
        print("✅ Gemini API ready")
        
        # -------------------------------------------------
        # 2. LOAD VECTOR DATABASE
        # -------------------------------------------------
        print("🗄️ Loading your vector database...")
        try:
            # Connect to ChromaDB directly (no LangChain issues)
            self.chroma_client = chromadb.PersistentClient(path=vector_db_path)
            
            # Try to get the collection
            try:
                self.collection = self.chroma_client.get_collection("coffee_shop_knowledge_base")
            except:
                # If collection doesn't exist, list available ones
                collections = self.chroma_client.list_collections()
                if collections:
                    self.collection = collections[0]  # Use first available
                    print(f"⚠️ Using collection: {self.collection.name}")
                else:
                    raise Exception("No collections found in vector_db!")
            
            count = self.collection.count()
            print(f"✅ Vector DB loaded: {count} items")
            
        except Exception as e:
            print(f"❌ Error loading vector DB: {e}")
            print("Trying to load with fallback method...")
            self.collection = None
        
        # -------------------------------------------------
        # 3. INITIALIZE CHAT HISTORY
        # -------------------------------------------------
        self.chat_history = []
        self.max_history = 5
        
        print("✅ Gemini RAG System ready!")
        print("-" * 50)
    
    def retrieve_context(self, query: str, k: int = 4) -> Tuple[str, List[Dict]]:
        """
        Retrieve relevant context from your vector DB
        """
        if not self.collection:
            return "Vector database not loaded.", []
        
        try:
            # Query ChromaDB directly
            results = self.collection.query(
                query_texts=[query],
                n_results=k,
                include=["documents", "metadatas"]
            )
            
            if not results['documents'] or not results['documents'][0]:
                return "No information available.", []
            
            # Format context
            context_parts = []
            docs = []
            
            for i, (doc_text, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0])):
                source = metadata.get('source', 'Unknown')
                doc_type = metadata.get('type', 'info')
                
                # Create document object
                doc = {
                    'page_content': doc_text,
                    'metadata': metadata
                }
                docs.append(doc)
                
                # Add to context
                context_parts.append(f"[Source: {source} | Type: {doc_type}]\n{doc_text}")
            
            context = "\n\n".join(context_parts)
            return context, docs
            
        except Exception as e:
            print(f"Retrieval error: {e}")
            return f"Error retrieving information: {str(e)[:50]}", []
    
    def format_prompt(self, query: str, context: str) -> str:
        """
        Format prompt with context
        """
        # Add chat history if available
        history_text = ""
        if self.chat_history:
            history_text = "PREVIOUS CONVERSATION:\n"
            for human_msg, ai_msg in self.chat_history[-3:]:  # Last 3 exchanges
                history_text += f"Customer: {human_msg}\n"
                history_text += f"Assistant: {ai_msg}\n"
            history_text += "\n"
        
        prompt = f"""You are BrewBot, a friendly and helpful assistant at "Nikunja Abir's Cafe" in Dhaka, Bangladesh.

IMPORTANT RULES:
1. ALWAYS use the provided information to answer questions
2. Be polite, friendly, and helpful
3. If you don't know something, say so politely
4. Keep answers concise but informative
5. Always mention prices in BDT (Bangladeshi Taka)
6. Promote special offers when relevant

{history_text}RELEVANT CAFE INFORMATION:
{context}

CURRENT QUESTION: {query}

Assistant (respond helpfully and concisely):
"""
        return prompt
    
    def generate_response(self, query: str) -> Tuple[str, str, List]:
        """
        Generate response using Gemini API + your vector DB
        """
        print(f"💭 Query: '{query}'")
        
        # 1. Retrieve context from YOUR database
        print("   🔍 Retrieving from your vector DB...")
        context, retrieved_docs = self.retrieve_context(query)
        
        # 2. Build prompt with your data
        prompt = self.format_prompt(query, context)
        
        # 3. Call Gemini API
        print("   ⚡ Calling Gemini API...")
        try:
            response = self.model.generate_content(prompt)
            answer = response.text.strip()
            
            print(f"✅ Response generated ({len(answer)} chars)")
            
            # Update chat history
            self.chat_history.append((query, answer))
            if len(self.chat_history) > self.max_history:
                self.chat_history = self.chat_history[-self.max_history:]
            
            return answer, context, retrieved_docs
            
        except Exception as e:
            error_msg = f"Sorry, API error: {str(e)[:100]}"
            return error_msg, context, retrieved_docs
    
    def clear_history(self):
        """Clear chat history"""
        self.chat_history = []
        print("🗑️ Chat history cleared")
    
    def test_system(self):
        """Test the Gemini RAG system"""
        print("\n" + "="*60)
        print("🧪 TESTING GEMINI + YOUR VECTOR DB")
        print("="*60)
        
        test_queries = [
            "What coffee drinks do you have?",
            "How much is a cappuccino?",
            "What are your opening hours?",
            "Do you have Bangladeshi tea?",
            "Any special offers today?"
        ]
        
        for query in test_queries:
            print(f"\n🧑 Customer: {query}")
            response, context, docs = self.generate_response(query)
            print(f"🤖 Assistant: {response}")
            
            if docs:
                sources = list(set([d['metadata'].get('source', '?') for d in docs]))
                print(f"   📚 Sources: {', '.join(sources)}")
        
        print("\n" + "="*60)
        print("✅ Gemini RAG Test Complete!")
        print("="*60)


# -------------------------------------------------
# TEST THE SYSTEM
# -------------------------------------------------
if __name__ == "__main__":
    print("="*60)
    print("☕ GEMINI API + YOUR VECTOR DB")
    print("="*60)
    
    # Your API key (hardcoded for testing)
    API_KEY = "GEMINI_API_KEY"
    
    if not API_KEY:
        print("❌ No API key provided!")
        print("Get free key from: GEMINI_API_KEY")
    else:
        try:
            # Initialize
            rag = GeminiCoffeeRAG(api_key=API_KEY)
            
            # Test
            rag.test_system()
            
            # Interactive chat
            print("\n" + "="*60)
            print("💬 CHAT WITH GEMINI + YOUR DATA")
            print("="*60)
            
            while True:
                user_input = input("\n🧑 You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit', 'bye', 'q']:
                    print("👋 Thank you for visiting Nikunja Abir's Cafe!")
                    break
                
                elif user_input.lower() == 'clear':
                    rag.clear_history()
                    continue
                
                # Generate response
                response, context, docs = rag.generate_response(user_input)
                print(f"\n🤖 BrewBot (Gemini): {response}")
                
                if docs:
                    print(f"   📚 Based on {len(docs)} documents from your DB")
                    
        except Exception as e:
            print(f"❌ Error: {e}")