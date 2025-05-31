import re
from langchain.schema import SystemMessage, HumanMessage, AIMessage

def format_messages(messages, documents=""):
    formatted = [SystemMessage(content=f"Você é um assistente virtual chamado Keiki e tem acesso às seguintes informações para dar suas respostas: {documents}")]
    for role, content in messages:
        if role == 'user':
            formatted.append(HumanMessage(content=content))
        elif role == 'assistant':
            formatted.append(AIMessage(content=content))
    return formatted

def format_text(text):
    if not isinstance(text, str):
        raise ValueError("O texto fornecido para format_text não é uma string.")
    return re.sub(r"\*\*(.*?)\*\*", lambda m: m.group(1).upper(), text)
