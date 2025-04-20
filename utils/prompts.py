def get_summary_prompt(ticket_text):
    return f"Summarize the customer's problem:\n\n{ticket_text}"

def get_action_prompt(ticket_text):
    return f"What actions should be taken for this issue?\n\n{ticket_text}"

def get_resolution_prompt(ticket_text, knowledge_base):
    return f"""Given the issue:\n{ticket_text}\n\nAnd this knowledge base:\n{knowledge_base}\n\nSuggest a resolution."""
