📄 Resume Search Chatbot (RAG)

A Retrieval-Augmented Generation (RAG) based chatbot built using Streamlit and LangChain, designed to intelligently search and analyze bulk resume PDFs. Users can upload multiple resumes and ask natural language questions to retrieve relevant candidate information.

🚀 Features
📂 Upload multiple resume PDFs at once
🔍 Semantic search across all resumes
🧠 Context-aware answers using OpenAI LLM
📄 Uses resume content as grounding (RAG)
⚡ Fast vector search with FAISS
🖥️ Simple and interactive Streamlit UI

Tech Stack
Frontend-	Streamlit
LLM	OpenAI- (ChatGPT)
Framework	LangChain- (1.2.0 – LCEL)
Vector DB-	FAISS
Embeddings-	OpenAI Embeddings
PDF Parsing-	PyPDF
Environment	-Python 3.10+

Create a .env file in the root folder:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

🧠 How It Works (Architecture)

PDF Upload – User uploads multiple resume PDFs

Text Extraction – Text extracted using PyPDF

Chunking – Resumes split into overlapping chunks

Embedding – Chunks converted into vectors

Vector Store – Stored in FAISS

Query – User asks a question

Retrieval – Relevant resume chunks fetched

LLM Response – Answer generated using retrieved context

💬 Example Queries

“Find candidates with Python and Django experience”

“Who has internship experience in data science?”

“Which resumes mention React and AWS?”

“Candidates with more than 2 years experience”
