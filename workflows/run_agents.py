from Agents.summary_agents import summarize_ticket
from Agents.action_agent import extract_actions
from Agents.resolution_agent import recommend_resolution
from Agents.routing_agent import route_ticket
from Agents.eta_agent import estimate_resolution_time
from Agents.routing_agent import is_relevant_query

def run_full_agentic_flow(ticket):
    description = ticket.get("description", "").strip()
    category = ticket.get("category", "").strip()
    
    if not description:
        return {"error": "Ticket description is empty."}
    
    # Guard against non-support queries
    if not is_relevant_query(description):
        return {
            "ticket_id": ticket.get("ticket_id", None),
            "message": "Sorry, I can only help with Samsung product support or related issues."
        }

    # Agentic processing
    try:
        summary = summarize_ticket(description)
        actions = extract_actions(description)
        resolution = recommend_resolution(description, category)
        routing = route_ticket(category)
        eta = estimate_resolution_time(category)

        return {
            "ticket_id": ticket.get("ticket_id", None),
            "summary": summary,
            "actions": actions,
            "recommended_fix": resolution,
            "route_to": routing,
            "eta": eta
        }

    except Exception as e:
        # Fail-safe response
        return {
            "ticket_id": ticket.get("ticket_id", None),
            "message": "We faced an issue while processing your request. It has been forwarded to our support team.",
            "error": str(e)
        }
