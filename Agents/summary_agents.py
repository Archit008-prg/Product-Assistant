from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from config.config import GOOGLE_API_KEY, TEMPERATURE

# def get_summary_agent():
#     llm = ChatGoogleGenerativeAI(api_key=GOOGLE_API_KEY, temperature=TEMPERATURE)
#     return llm


def get_summary_agent():
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-pro-latest", 
        api_key=GOOGLE_API_KEY, 
        temperature=TEMPERATURE
    )
    return lambda query: llm.invoke([HumanMessage(content=query)])


def summarize_ticket(description):
    agent = get_summary_agent()
    prompt = f"Summarize this customer issue: {description}"
    return agent(prompt)
