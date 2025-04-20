import json
from workflows.run_agents import run_full_agentic_flow

with open("data/ticket_examples.json") as f:
    tickets = json.load(f)

for ticket in tickets:
    result = run_full_agentic_flow(ticket)
    print(json.dumps(result, indent=2))
