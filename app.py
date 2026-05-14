from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime
import os

# importar IA (nuevo)
from ollama_modelo import analizar_sintomas

app = Flask(__name__)
CORS(app)

# Cargar datos y entrenar modelo
datos = pd.read_csv("datos_salud.csv", sep=";")
df = pd.DataFrame(datos)

X = df[["temperatura", "frecuencia_cardiaca", "presion_sistolica"]]
y = df["estado"]

modelo = DecisionTreeClassifier()
modelo.fit(X, y)

variables = [
    "temperatura",
    "frecuencia_cardiaca",
    "presion_sistolica"
]

def variable_influyente():

    importancias = modelo.feature_importances_

    indice = importancias.argmax()

    return variables[indice]

# Función de recomendación
def recomendacion(estado, temperatura, frecuencia, presion):

    mensajes = []

    if estado == "normal":

        mensajes.append(
            "Estado normal. Continúe monitoreando su salud."
        )

    elif estado == "alerta_media":

        mensajes.append("Alerta media.")

        if temperatura > 37.5:
            mensajes.append(
                "Posible fiebre, hidrátese y descanse."
            )

        if frecuencia > 100:
            mensajes.append(
                "Frecuencia cardíaca elevada."
            )

        if presion > 130:
            mensajes.append(
                "Presión arterial elevada."
            )

    elif estado == "alerta_alta":

        mensajes.append(
            "Alerta alta. Consulte con un médico inmediatamente."
        )

    return mensajes

# Guardar historial
def guardar_historial(temperatura, frecuencia, presion, estado):

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nuevo_registro = pd.DataFrame([{
        "fecha": fecha_hora,
        "temperatura": temperatura,
        "frecuencia_cardiaca": frecuencia,
        "presion_sistolica": presion,
        "estado": estado
    }])

    archivo_existe = os.path.isfile("historial_salud.csv")

    nuevo_registro.to_csv(
        "historial_salud.csv",
        mode="a",
        header=not archivo_existe,
        index=False
    )

# Ruta principal (tu sistema actual)
@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None
    recomendaciones = []

    if request.method == "POST":
        temperatura = float(request.form["temperatura"])
        frecuencia = int(request.form["frecuencia"])
        presion = int(request.form["presion"])

        nuevo_dato = pd.DataFrame(
            [[temperatura, frecuencia, presion]],
            columns=["temperatura", "frecuencia_cardiaca", "presion_sistolica"]
        )

        prediccion = modelo.predict(nuevo_dato)[0]

        recomendaciones = recomendacion(prediccion, temperatura, frecuencia, presion)

        guardar_historial(temperatura, frecuencia, presion, prediccion)

        resultado = prediccion

    return render_template("index.html", resultado=resultado, recomendaciones=recomendaciones)

#Chat 
@app.route("/chat")
def chat():
    return render_template("chat.html")

# NUEVA RUTA IA (síntomas)
@app.route("/sintomas", methods=["POST"])
def sintomas():

    texto = request.form["sintomas"]

    try:
        respuesta = analizar_sintomas(texto)
    except Exception as e:
        respuesta = str(e)

    return render_template("chat.html", respuesta=respuesta)

@app.route("/api/chat", methods=["POST"])
def api_chat():

    data = request.get_json()

    texto = data.get("mensaje")
    
    perfil = data.get("perfil", {})

    try:
        respuesta = analizar_sintomas(texto, perfil)

    except Exception as e:
        respuesta = str(e)

    return jsonify({
        "respuesta": respuesta
    })
    
@app.route("/api/monitor", methods=["POST"])
def monitor():

    data = request.json

    temperatura = float(data["temperatura"])

    frecuencia = int(data["frecuencia"])

    presion = int(data["presion"])

    nuevo_dato = pd.DataFrame(
        [[temperatura, frecuencia, presion]],
        columns=[
            "temperatura",
            "frecuencia_cardiaca",
            "presion_sistolica"
        ]
    )

    prediccion = modelo.predict(nuevo_dato)[0]

    recomendaciones = recomendacion(
        prediccion,
        temperatura,
        frecuencia,
        presion
    )

    guardar_historial(
        temperatura,
        frecuencia,
        presion,
        prediccion
    )

    return jsonify({

        "estado": prediccion,

        "recomendaciones": recomendaciones,

        "variable_importante": variable_influyente()
    })

if __name__ == "__main__":
    app.run(debug=True)