import os
from pathlib import Path
from dotenv import load_dotenv
from ollama import Client

# cargar .env
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# obtener api key
api_key = os.getenv("OLLAMA_API_KEY")

print("API KEY:", api_key)

# cliente
client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": api_key
    }
)


def analizar_sintomas(texto, perfil):
    
    contexto_medico = f"""
INFORMACIÓN MÉDICA DEL PACIENTE:

Nombre: {perfil.get('nombre', '')}
Edad: {perfil.get('edad', '')}
Peso: {perfil.get('peso', '')} libras
Altura: {perfil.get('altura', '')} cm
Género: {perfil.get('genero', '')}

Alergias:
{perfil.get('alergias', 'Ninguna')}

Enfermedades crónicas:
{perfil.get('enfermedades', 'Ninguna')}

Medicamentos:
{perfil.get('medicamentos', 'Ninguno')}
"""

    prompt = f"""
Eres un asistente médico con inteligencia artificial.

INFORMACIÓN DEL PACIENTE:
{contexto_medico}

Tu objetivo es responder de forma cercana, humana y fácil de entender.

IMPORTANTE:
- Háblale al usuario de "tú"
- Usa un tono amable, tranquilo y profesional
- Explica las cosas de forma sencilla
- Puedes usar términos médicos, pero explícalos fácil
- No uses lenguaje técnico complicado
- No suenes como un reporte médico
- No hagas respuestas demasiado largas
- Usa párrafos cortos
- No uses markdown
- No uses símbolos como *, # o **

MUY IMPORTANTE:
- La información médica del perfil es SOLO contexto
- NO hagas un resumen del perfil del usuario
- SOLO menciona datos del perfil si realmente tienen relación con el síntoma o pregunta
- No fuerces conexiones entre el perfil médico y los síntomas
- No menciones alergias, enfermedades o medicamentos si no tienen relación clara con la consulta
- Si el perfil no aporta información útil para la respuesta, simplemente ignóralo
- Nunca inventes relaciones médicas solo para usar información del perfil

La respuesta debe sentirse natural y generar confianza.

Usa esta estructura:

Por lo que describes:
(explicación breve y humana)

Lo que te recomiendo hacer:
1. recomendación
2. recomendación
3. recomendación

Advertencias:
(indicar cuándo debería consultar a un médico)
{texto}
"""

    response = client.chat(
        model="gemma3:4b-cloud",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    respuesta = response["message"]["content"]

    # limpiar markdown y símbolos
    respuesta = respuesta.replace("*", "")
    respuesta = respuesta.replace("#", "")

    return respuesta

    return response["message"]["content"]