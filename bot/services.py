import requests
from config.settings import GROQ_API_KEY, WEATHER_API_KEY
from langchain_community.document_loaders.web_base import WebBaseLoader
from PyPDF2 import PdfReader

def fetch_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"O clima em {city} é {weather} com temperatura de {temperature}°C."
        else:
            return f"Não foi possível obter informações sobre o clima em {city}."
    except Exception as e:
        return f"Erro ao acessar a API do Clima: {e}"

def fetch_world_current_time(timezone):
    try:
        url = f"http://worldtimeapi.org/api/timezone/{timezone}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            datetime_str = data["datetime"].replace("Z", "+00:00")
            return datetime_str
        else:
            return "Erro ao acessar a API de hora."
    except Exception as e:
        return f"Erro ao acessar a API de hora: {e}"

def fetch_website_content(url):
    try:
        loader = WebBaseLoader(url)
        documents = loader.load()
        return "\n".join(doc.page_content for doc in documents)
    except Exception as e:
        return f"Erro ao acessar o site {url}: {e}"

def fetch_pdf_content(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            content = ""
            for page in reader.pages:
                content += page.extract_text()
            return content
    except Exception as e:
        return f"Erro ao acessar o PDF: {e}"
