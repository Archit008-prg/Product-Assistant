from Agents.summary_agents import get_summary_agent


def extract_actions(description):
    agent = get_summary_agent()  # reuse same LLM
    prompt = f"From the customer's issue, extract actionable steps like 'escalate', 'log request', or 'replace item': {description}"
    return agent(prompt)
