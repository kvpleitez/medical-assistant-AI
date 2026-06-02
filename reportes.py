from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from datetime import datetime
import tempfile

from ollama_modelo import generar_resumen_clinico

def limpiar_texto(texto):
    return (
        str(texto)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", " ")
        .replace("\r", " ")
    )

def crear_pdf_clinico(consultas, perfil):
    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )
    doc = SimpleDocTemplate(
        temp.name,
        pagesize=letter
    )
    styles = getSampleStyleSheet()
    elementos = []

    elementos.append(
        Paragraph(
            "Reporte Clínico Generado por IA",
            styles["Title"]
        )
    )
    elementos.append(Spacer(1, 20))

    elementos.append(
        Paragraph(
            "Este informe fue generado mediante inteligencia artificial y no reemplaza la evaluación de un médico profesional.",
            styles["BodyText"]
        )
    )
    elementos.append(Spacer(1, 20))

    elementos.append(
        Paragraph(
            f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            styles["BodyText"]
        )
    )
    elementos.append(Spacer(1, 30))
    
    elementos.append(
    Paragraph(
        "Datos del paciente",
        styles["Heading1"]
    )
)

    elementos.append(
        Paragraph(
            f"""
            Nombre: {perfil.get('nombre', 'No registrado')}<br/>
            Edad: {perfil.get('edad', 'No registrada')} años<br/>
            Género: {perfil.get('genero', 'No registrado')}<br/>
            Peso: {perfil.get('peso', 'No registrado')} lb<br/>
            Altura: {perfil.get('altura', 'No registrada')} cm
            """,
            styles["BodyText"]
        )
    )

    elementos.append(Spacer(1, 20))

    for consulta in consultas:
        sintomas_original = consulta.get(
            "sintomas",
            ""
        )

        sintomas = limpiar_texto(
            sintomas_original
        )

        resumen_clinico = generar_resumen_clinico(
            sintomas_original,
            {}
        )

        print("RESUMEN CLINICO:")
        print(resumen_clinico)

        respuesta = limpiar_texto(
            resumen_clinico
        )

        elementos.append(
            Paragraph("Motivo de consulta", styles["Heading2"])
        )
        elementos.append(
            Paragraph(sintomas, styles["BodyText"])
        )
        elementos.append(Spacer(1, 15))

        elementos.append(
            Paragraph("Análisis generado por IA", styles["Heading2"])
        )
        elementos.append(
            Paragraph(respuesta, styles["BodyText"])
        )
        elementos.append(Spacer(1, 30))

    doc.build(elementos)
    return temp.name