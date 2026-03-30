from rag.knowledge import KNOWLEDGE_BASE

def retrieve_context(query: str):
    results = []

    for item in KNOWLEDGE_BASE:
        if item["tag"] in query.lower():
            results.append(item["content"])

   
    if not results:
        results = [item["content"] for item in KNOWLEDGE_BASE]

    return "\n".join(results)