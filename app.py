import streamlit as st
import tempfile
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from utils import load_and_process_pdfs

load_dotenv()

st.set_page_config(page_title="Resume RAG Bot", layout="wide")
st.title("📄 Resume Search Chatbot (RAG)")

uploaded_files = st.file_uploader(
    "Upload bulk resume PDFs",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Processing resumes..."):
        temp_files = []

        for file in uploaded_files:
            temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            temp.write(file.read())
            temp.close()
            temp_files.append(temp.name)

        vectorstore = load_and_process_pdfs(temp_files)
        retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0
        )

        prompt = ChatPromptTemplate.from_template(
            """You are an HR assistant.
Use the following resume context to answer the question.

Context:
{context}

Question:
{question}

Answer clearly and concisely."""
        )

        rag_chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
        )

    st.success("Resumes processed successfully!")

    query = st.text_input("Ask about candidates:")

    if query:
        with st.spinner("Searching resumes..."):
            response = rag_chain.invoke(query)

        st.subheader("📌 Answer")
        st.write(response.content)
