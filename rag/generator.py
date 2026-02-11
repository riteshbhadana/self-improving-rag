from dotenv import load_dotenv
load_dotenv()

import time
from groq import InternalServerError
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def generate_answer(query, docs):
    context = "\n\n".join([d.page_content[:900] for d in docs])

    prompt = f"""
You are an information extraction assistant.

insight, reasoning if any read output they will impresed.

Rules:
- Do NOT summarize
- Do NOT shorten
- List everything explicitly
- Organize into categories if possible
- Use bullet points
- Only use information from the context

Context:
{context}

Question:
{query}
"""

    retries = 3
    delay = 2

    for attempt in range(retries):
        try:
            response = llm.invoke(prompt)

            content = response.content
            return content if isinstance(content, str) else str(content)

        except InternalServerError:
            print(f"Groq overloaded. Retry {attempt+1}/{retries}")
            time.sleep(delay)
            delay *= 2

        except Exception as e:
            print("GENERATOR ERROR:", e)
            return "⚠️ Model error. Please try again."

    return "⚠️ Groq overloaded. Try again in a few seconds."
