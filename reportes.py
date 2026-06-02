from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
import tempfile

from ollama_modelo import (
    generar_resumen_clinico,
    generar_motivo_consulta
)

def limpiar_texto(texto):
    return (
        str(texto)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
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

    disclaimer = Table(
        [[
            """
            AVISO IMPORTANTE

            Este informe fue generado mediante inteligencia artificial.
            No constituye un diagnóstico médico y no sustituye la evaluación de un profesional de la salud.
            """
        ]],
        colWidths=[500]
    )

    disclaimer.setStyle(
        TableStyle([
            ('BOX', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), colors.lightgrey),
            ('PADDING', (0,0), (-1,-1), 10),
        ])
    )

    elementos.append(disclaimer)
    elementos.append(Spacer(1,20))

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
    
    elementos.append(
        Paragraph(
            "Antecedentes Personales",
            styles["Heading1"]
        )
    )
    
    alergias = perfil.get(
        "alergias",
        "No registradas"
    )

    elementos.append(
        Paragraph(
            f"<b>Alergias:</b> {alergias}",
            styles["BodyText"]
        )
    )

    medicamentos = perfil.get(
        "medicamentos",
        "No registrados"
    )

    elementos.append(
        Paragraph(
            f"<b>Medicamentos habituales:</b> {medicamentos}",
            styles["BodyText"]
        )
    )
    
    enfermedades = perfil.get(
        "enfermedades",
        "No registradas"
    )

    elementos.append(
        Paragraph(
            f"<b>Antecedentes médicos:</b> {enfermedades}",
            styles["BodyText"]
        )
    )
    

    elementos.append(Spacer(1, 20))

    for consulta in consultas:
        sintomas_original = consulta.get(
            "sintomas",
            ""
        )

        motivo_consulta = generar_motivo_consulta(
            sintomas_original
        )

        motivo_consulta = limpiar_texto(
            motivo_consulta
        )

        resumen_clinico = generar_resumen_clinico(
            sintomas_original,
        )

        print("RESUMEN CLINICO:")
        print(resumen_clinico)

        respuesta = limpiar_texto(
            resumen_clinico
        )
        
        respuesta = respuesta.replace(
            "\n",
            "<br/>"
        )

        elementos.append(
            Paragraph("Motivo de consulta", styles["Heading2"])
        )
        elementos.append(
            Paragraph(motivo_consulta, styles["BodyText"])
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