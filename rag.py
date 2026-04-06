documents = [
    "AI is the future of technology.",
    "Machine learning is a subset of AI.",
    "Python is widely used in AI and data science."
]

def retrieve(query):
    results = []
    for doc in documents:
        if any(word.lower() in doc.lower() for word in query.split()):
            results.append(doc)
    return results

def generate_answer(query):
    retrieved_docs = retrieve(query)
    
    if not retrieved_docs:
        return "No relevant information found."
    
    return " ".join(retrieved_docs)

query = input("Ask something: ")
print("Answer:", generate_answer(query))
