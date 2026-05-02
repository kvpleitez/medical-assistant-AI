import cv2
import os

carpeta_usuarios = "usuarios"

# Crear carpeta si no existe
if not os.path.exists(carpeta_usuarios):
    os.makedirs(carpeta_usuarios)


# Registrar usuario
def registrar_usuario():
    nombre = input("Ingrese el nombre del nuevo usuario: ").strip()
    ruta_imagen = os.path.join(carpeta_usuarios, f"{nombre}.jpg")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: no se pudo acceder a la cámara")
        return

    print("Presione 's' para tomar la foto o 'q' para cancelar")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error al capturar imagen")
            break

        cv2.imshow("Registro de usuario", frame)

        tecla = cv2.waitKey(1) & 0xFF

        if tecla == ord('s'):
            cv2.imwrite(ruta_imagen, frame)
            print(f"Usuario {nombre} registrado correctamente")
            break
        elif tecla == ord('q'):
            print("Registro cancelado")
            break

    cap.release()
    cv2.destroyAllWindows()


# Iniciar sesión
def iniciar_sesion():
    print("Iniciando reconocimiento facial")

    if len(os.listdir(carpeta_usuarios)) == 0:
        print("No hay usuarios registrados")
        return None

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: no se pudo acceder a la cámara")
        return None

    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Error al capturar imagen")
        return None

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.resize(gray_frame, (200, 200))

    nombre_reconocido = None
    mejor_coincidencia = float("inf")

    for archivo in os.listdir(carpeta_usuarios):
        ruta = os.path.join(carpeta_usuarios, archivo)

        imagen_guardada = cv2.imread(ruta)

        if imagen_guardada is None:
            continue

        imagen_guardada = cv2.cvtColor(imagen_guardada, cv2.COLOR_BGR2GRAY)
        imagen_guardada = cv2.resize(imagen_guardada, (200, 200))

        diferencia = cv2.absdiff(gray_frame, imagen_guardada)
        score = cv2.sumElems(diferencia)[0]

        if score < mejor_coincidencia:
            mejor_coincidencia = score
            nombre_reconocido = archivo.split(".")[0]

    umbral = 5000000

    if mejor_coincidencia < umbral:
        texto = f"Usuario: {nombre_reconocido}"
    else:
        texto = "Desconocido"
        nombre_reconocido = None

    cv2.putText(frame, texto, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    cv2.imshow("Reconocimiento facial", frame)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

    print(texto)

    return nombre_reconocido


# Programa principal
def main():
    print("Asistente robótico inteligente")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        usuario = iniciar_sesion()

        if usuario:
            print(f"Bienvenido/a {usuario}")
        else:
            print("Usuario no reconocido")
    else:
        print("Opción no válida")


main()