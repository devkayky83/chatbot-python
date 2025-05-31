import re
from .services import fetch_weather, fetch_world_current_time, fetch_website_content, fetch_pdf_content
from .utils import format_messages, format_text
from langchain_groq import ChatGroq

chat = ChatGroq(model='llama-3.3-70b-versatile')

def time_request(message):
    match = re.search(r"hora(?:\s+em)?\s+([\w/_\-]+)", message, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def bot_answer(messages):
    try:
        if not messages:
            return "A lista de mensagens está vazia, envie uma mensagem para começar."
        
        last_message = messages[-1][1]
        
        # Certificando que a ultima mensagem é uma string
        if not isinstance(last_message, str):
            return "A última mensagem não é válida, por favor, envie uma mensagem de texto."
        
        # Inicializa as variáveis para garantir que sempre tenham um valor
        url_content = ""
        pdf_content = ""

        # Procurar URL na última mensagem
        url_match = re.search(r'(https?://\S+)', last_message)
        if url_match:
            url = url_match.group(1)
            url_content = fetch_website_content(url)
            if "Erro" in url_content:
                return url_content
        else:
            url_content = "Nenhum site foi acessado nesta interação."

        # Verifica se é um link para um PDF
        pdf_match = re.search(r'(\S+\.pdf)', last_message)
        if pdf_match:
            pdf_url = pdf_match.group(1)
            pdf_content = fetch_pdf_content(pdf_url)
            if "Erro" in pdf_content:
                return pdf_content
        else:
            pdf_content = "Nenhum PDF foi acessado nesta interação."
        
        # Verifica se a mensagem está relacionada ao clima
        if "clima em" in last_message.lower():
            city_match = re.search(r"clima(?: em)? ([\w\s]+)", last_message.lower())
            if city_match:
                city = city_match.group(1).strip()
                return fetch_weather(city)
            else:
                return "Por favor, informe a cidade no formato 'clima em [cidade]'."
        
        # Verifica se a mensagem está relacionada à hora
        if "hora" in last_message.lower() or "horas" in last_message.lower():
            timezone = time_request(last_message)
            if timezone:
                return fetch_world_current_time(timezone)
            else:
                return "Não foi possível retornar a hora como pedido."
            
        # Formatar e enviar para o modelo
        model_messages = format_messages(messages, documents=last_message)
        response = chat.invoke(model_messages)
        
        formated_response = format_text(response.content)
        return formated_response
    except Exception as e:
        return f"Erro em bot_answer: {e}"
