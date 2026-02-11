from langgraph.graph import StateGraph, END
from rag.generator import generate_answer
from evaluation.evaluator import evaluate_answer


def retrieve_node(state):
    query = state["query"]
    retriever = state["retriever"]

    docs = retriever.invoke(query)

    return {
        "query": query,
        "retriever": retriever,   # ✅ pass forward
        "docs": docs
    }


def generate_node(state):
    query = state["query"]
    retriever = state["retriever"]
    docs = state["docs"]

    answer = generate_answer(query, docs)

    return {
        "query": query,
        "retriever": retriever,   # ✅ pass forward
        "docs": docs,
        "answer": answer
    }


def evaluate_node(state):
    query = state["query"]
    retriever = state["retriever"]
    docs = state["docs"]
    answer = state["answer"]

    score = evaluate_answer(answer, docs)

    return {
        "query": query,
        "retriever": retriever,   # ✅ pass forward
        "docs": docs,
        "answer": answer,
        "score": score
    }


def should_retry(state):
    return state["score"] < 0.7


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate", generate_node)
    graph.add_node("evaluate", evaluate_node)

    graph.set_entry_point("retrieve")

    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", "evaluate")

    graph.add_conditional_edges(
        "evaluate",
        should_retry,
        {
            True: "retrieve",
            False: END
        }
    )

    return graph.compile()
