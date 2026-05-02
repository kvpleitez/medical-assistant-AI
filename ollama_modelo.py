import os
from ollama import Client

# configurar cliente
client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": "e27de7a5885746a2a2794b0ec79819a7.BPXwVg39QJL_efNA0QwI5rr8"
    }
)

def analizar_sintomas(texto):

    prompt = f"""
Eres un asistente médico básico.

Responde de forma clara y ordenada:
- Usa párrafos cortos
- No uses símbolos como ** o *
- Usa frases simples
- Separa recomendaciones en líneas

Incluye advertencia de consultar a un médico.

Síntomas: {texto}
"""

    response = client.chat(
        model="gemma3:4b-cloud",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]