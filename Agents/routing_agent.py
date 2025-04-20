def route_ticket(category):
    routing_map = {
        "Smartphones": "Mobile Support Team",
        "Televisions": "Home Entertainment Team",
        "Laptops": "IT Support",
        "Air Conditioners": "Appliance Repair Team"
    }
    return routing_map.get(category, "General Support Team")

# Agents/routing_agent.py

import re

def is_relevant_query(query: str) -> bool:
    """
    Checks if the query is relevant to Samsung product support.
    Returns True if it's relevant, False if it's off-topic.
    """
    irrelevant_keywords = [
        "joke", "weather", "politics", "religion", "story", "news",
        "song", "movie", "game", "chat", "who are you", "openai",
        "tell me about yourself", "non-product", "funny", "flirt"
    ]

    lowered_query = query.lower()
    for keyword in irrelevant_keywords:
        if keyword in lowered_query:
            return False

    return True

