import streamlit as st
from rag.loader import load_documents
from rag.retriever import create_retriever
from graph.rag_graph import build_graph
from memory.feedback_store import save_feedback
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Self-Improving RAG", layout="wide")
st.title("🧠 Self-Improving RAG ")

pdf = st.file_uploader("Upload a PDF", type="pdf")

if pdf:
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())

    docs = load_documents("temp.pdf")
    retriever = create_retriever(docs)
    graph = build_graph()

    query = st.text_input("Ask a question")

    if query:
        result = graph.invoke({
            "query": query,
            "retriever": retriever
        })

        answer = result["answer"]
        score = result["score"]

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Evaluation Score")
        st.write(score)

        # 👍 / 👎 feedback buttons
        col1, col2 = st.columns(2)

        if col1.button("👍 Helpful"):
            save_feedback(query, answer, score, "positive")
            st.success("Feedback saved!")

        if col2.button("👎 Not Helpful"):
            save_feedback(query, answer, score, "negative")
            st.warning("Feedback saved!")
