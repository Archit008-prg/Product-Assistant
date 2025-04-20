import sys
import os
sys.path.append(os.path.abspath(".."))



import streamlit as st 
from workflows.run_agents import run_full_agentic_flow
from Agents.routing_agent import is_relevant_query

st.set_page_config(page_title="Samsung AI Support (Multi-Agent)", layout="centered")
st.title("🤖 Samsung Multi-Agent AI Customer Support")
st.markdown("Get support powered by intelligent multi-agent workflows.")

# 📩 Input form
user_query = st.text_area("📨 Paste the customer's issue here:", height=150)
ticket_id = st.text_input("🎫 Ticket ID (optional)", value="TICKET-001")
category = st.selectbox("📂 Choose product category", ["Smartphone", "TV", "Tablet", "Appliance", "Other"])

if st.button("🧠 Run Multi-Agent Support System"):
    if user_query.strip():
        with st.spinner("🤔 Processing through intelligent agents..."):

            # Check for relevant Samsung-related query
            if not is_relevant_query(user_query):
                st.warning("🚫 This assistant is only trained to help with Samsung product support or related issues.")
            else:
                ticket = {
                    "ticket_id": ticket_id,
                    "description": user_query,
                    "category": category
                }
                response = run_full_agentic_flow(ticket)

                if "error" in response:
                    st.error(f"❌ Error: {response['error']}")
                elif "message" in response:
                    st.info(f"ℹ️ {response['message']}")
                else:
                    st.markdown("### 📋 Support Summary")
                    st.markdown(response["summary"])

                    st.markdown("### 🛠️ Recommended Actions")
                    for i, action in enumerate(response["actions"], 1):
                        st.markdown(f"{i}. {action}")

                    st.markdown("### 🧩 Recommended Fix")
                    st.markdown(response["recommended_fix"])

                    st.markdown("### 🚚 Routed To")
                    st.markdown(response["route_to"])

                    st.markdown("### ⏱️ Estimated Time to Resolution")
                    st.markdown(response["eta"])
    else:
        st.warning("⚠️ Please enter a valid support-related query.")
    
