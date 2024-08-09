import os

def retrieve_memories(query, memories_dir="Memories"):
    """Searches for relevant memories based on keyword matching."""
    relevant_memories = []
    for filename in os.listdir(memories_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(memories_dir, filename), "r", encoding='utf-8') as f:
                text = f.read()
                if any(keyword in text.lower() for keyword in query.lower().split()):
                    relevant_memories.append(text)
    return relevant_memories
