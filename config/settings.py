import os 
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

if not GROQ_API_KEY or not WEATHER_API_KEY:
    raise ValueError("Chaves de API não foram configuradas corretamente! (Verifique o arquivo .env)")

# Definindo o USER_AGENT no ambiente global
os.environ['USER_AGENT'] = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/110.0.0.0 Safari/537.36 OPR/95.0.0.0'
    ' OR '
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/110.0.0.0 Safari/537.36 OPR/95.0.0.0'
    ' OR '
    'Mozilla/5.0 (X11; Linux; X86_64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/110.0.0.0 Safari/537.36 OPR/95.0.0.0'
)