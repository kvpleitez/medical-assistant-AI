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
        model="gemma4:cloud",
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

#Función para generar report
def generar_reporte_ia(historial):

    prompt = f"""
Eres un sistema profesional de análisis médico con inteligencia artificial.

Tu tarea es generar un informe clínico automatizado basado en el historial del usuario.

IMPORTANTE:
- NO respondas como chat
- NO uses frases conversacionales
- NO uses expresiones como:
  "okay"
  "aquí tienes"
  "espero que te sirva"
- NO hagas introducciones informales
- NO uses markdown
- NO uses asteriscos
- NO uses símbolos como # o **
- NO uses listas con viñetas
- Usa lenguaje profesional y humano
- Usa títulos simples
- Mantén formato limpio y ordenado
- Usa párrafos cortos
- Usa enumeraciones normales únicamente cuando sea necesario

Estructura obligatoria:

Resumen general:
texto

Síntomas frecuentes:
texto

Patrones identificados:
texto

Posibles riesgos:
texto

Recomendaciones generales:
1. texto
2. texto
3. texto

Advertencia:
texto breve

El reporte debe sentirse como un informe clínico profesional generado automáticamente.

Historial del usuario:
{historial}
"""

    response = client.chat(
        model="gemma4:cloud",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

def generar_resumen_clinico(
    sintomas,
):
    prompt = f"""
Actúa como un asistente de documentación clínica.

Tu tarea es redactar un resumen clínico profesional basado EXCLUSIVAMENTE en la información proporcionada por el paciente.

REGLAS OBLIGATORIAS:

* No inventes síntomas.
* No inventes duración de síntomas.
* No inventes antecedentes médicos.
* No inventes exploraciones físicas.
* No inventes signos vitales.
* No inventes resultados de laboratorio.
* No inventes estudios diagnósticos.
* No asumas enfermedades a partir del perfil médico.
* No utilices alergias, enfermedades crónicas o medicamentos del perfil para formular diagnósticos, a menos que el paciente los mencione explícitamente en la consulta actual.
* No emitas diagnósticos definitivos.
* No indiques suspender, iniciar o modificar medicamentos.

ESTILO:

* Utiliza lenguaje clínico de nivel intermedio.
* Siempre que sea posible, combina el término médico con una explicación sencilla.
* Evita frases excesivamente técnicas o académicas.
* Evita texto repetitivo.
* Redacción breve, clara y profesional.

Consulta actual:
{sintomas}

Genera únicamente:

Padecimiento actual:
Descripción objetiva de los síntomas reportados.

Impresión diagnóstica:
Posibles causas compatibles con los síntomas descritos, indicando que se trata de una valoración orientativa generada por IA.

Recomendaciones generales:
Medidas generales de cuidado y vigilancia. Indicar valoración médica si los síntomas persisten o empeoran.

Extensión máxima: 120 palabras.

"""
    response = client.chat(
        model="gemma4:cloud",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    respuesta = response["message"]["content"]

    # limpiar markdown y símbolos
    respuesta = respuesta.replace("*", "")
    respuesta = respuesta.replace("#", "")

    return respuesta

def generar_motivo_consulta(sintomas):

    prompt = f"""
Actúa como un redactor clínico profesional.

Convierte el texto del paciente en un motivo de consulta breve y formal.

Reglas:
- Máximo una oración.
- Redacción impersonal.
- No usar primera persona.
- No usar comillas.
- No usar listas.
- Lenguaje clínico.

Ejemplos:

Paciente:
"me duele mucho el cuello cuando lo muevo"

Motivo de consulta:
Dolor cervical asociado a movimientos laterales del cuello.

Paciente:
"tengo la nariz tapada y estornudo mucho"

Motivo de consulta:
Congestión nasal y episodios frecuentes de estornudos.

Paciente:
"ya me tomé una loratadina y no mejora"

Motivo de consulta:
Persistencia de síntomas alérgicos pese al uso de antihistamínico.

Texto del paciente:
{sintomas}
"""

    response = client.chat(
        model="gemma4:cloud",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]