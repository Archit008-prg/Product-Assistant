import json

def load_tickets(path):
    with open(path, "r") as f:
        return json.load(f)

def load_knowledge_base(path):
    with open(path, "r") as f:
        return json.load(f)
