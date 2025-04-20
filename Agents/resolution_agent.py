import json

from Agents.summary_agents import get_summary_agent
def load_knowledge_base():
    with open("data/knowledge_base.json") as f:
        return json.load(f)

def recommend_resolution(description, category):
    knowledge_base = load_knowledge_base()
    common_issues = knowledge_base.get(category, [])
    
    agent = get_summary_agent()
    prompt = f"The issue is: {description}. Based on the following known resolutions: {common_issues}, suggest a fix."
    return agent(prompt)
