import os
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

api_key = os.getenv("OLLAMA_API_KEY")

client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": api_key
    }
)

def analizar_sintomas(texto):

    prompt = f"""
Eres un asistente médico con inteligencia artificial.

Tu respuesta debe verse profesional, clara y fácil de leer.

Reglas IMPORTANTES:
- Responde usando varios párrafos
- Deja una línea en blanco entre ideas
- Usa lenguaje sencillo
- No uses markdown
- No uses símbolos como * o #

Estructura:
Posible análisis:
Recomendaciones:
Advertencia:

Síntomas:
{texto}
"""

    response = client.chat(
        model="gemma3:4b-cloud",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]