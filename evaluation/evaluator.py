from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

judge_llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def evaluate_answer(answer, docs):
    context = "\n\n".join([d.page_content[:800] for d in docs])

    prompt = f"""
Score the answer from 0 to 1.

Answer:
{answer}

Context:
{context}

Return ONLY a number.
"""

    try:
        return float(judge_llm.invoke(prompt).content)
    except:
        return 0.0
