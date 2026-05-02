# Importar las librerías que se van a usar
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime
import os

# En base a investigaciones,
# Se va a tomar en cuenta temperatura, frecuencia cardíaca y presión sistólica
# La presión sistólica es la medición máxima de la presión arterial

datos = pd.read_csv("datos_salud.csv", sep=";")

df = pd.DataFrame(datos)

X = df[["temperatura", "frecuencia_cardiaca", "presion_sistolica"]]
y = df["estado"]

# Entrenamiento del modelo

modelo = DecisionTreeClassifier()
modelo.fit(X, y)

# Lista de variables que usa el modelo
variables = ["temperatura", "frecuencia_cardiaca", "presion_sistolica"]


# Función para pedirle al usuario sus mediciones
# Posteriormente esto será con sensores

def pedir_datos():

    # Validamos que los datos ingresados sean números
    while True:
        try:
            temperatura = float(input("Ingrese la temperatura corporal: "))
            frecuencia = int(input("Ingrese la frecuencia cardíaca: "))
            presion = int(input("Ingrese la presión sistólica: "))
            return temperatura, frecuencia, presion
        except ValueError:
            print("Error: ingrese valores numéricos válidos.\n")


# Función que da recomendaciones según el estado

def recomendacion(estado, temperatura, frecuencia, presion):

    if estado == "normal":
        print("Estado normal. Continúe monitoreando su salud.")

    elif estado == "alerta_media":
        print("Alerta media.")
        
        if temperatura > 37.5:
            print("- Posible fiebre, hidrátese y descanse.")
        if frecuencia > 100:
            print("- Frecuencia cardíaca elevada.")
        if presion > 130:
            print("- Presión arterial elevada.")

    elif estado == "alerta_alta":
        print("Alerta alta. Se recomienda consultar con un médico inmediatamente.")


# Función para mostrar qué variable influyó más en la decisión del modelo

def mostrar_variable_influyente():

    importancias = modelo.feature_importances_

    indice_mayor = importancias.argmax()

    variable_mas_importante = variables[indice_mayor]

    print("Variable que más influyó en la decisión:", variable_mas_importante)

#Función para guardar el historial
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
        
