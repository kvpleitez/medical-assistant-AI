# 🩺 Asistente Médico con Inteligencia Artificial

Aplicación web desarrollada con **React, Flask, Firebase y Machine Learning** que integra un asistente médico impulsado por inteligencia artificial para brindar orientación básica en salud, monitorear signos vitales y gestionar información médica personalizada de cada usuario.

> **Nota:** Este proyecto fue desarrollado con fines académicos y educativos. Las recomendaciones proporcionadas por el asistente no sustituyen la opinión de un profesional de la salud.

---

# 🚀 Tecnologías utilizadas

## Frontend

- React
- Vite
- CSS

## Backend

- Python
- Flask
- Flask-CORS

## Base de datos y autenticación

- Firebase Authentication
- Cloud Firestore

## Inteligencia Artificial

- Gemma 3 (OpenRouter)
- Machine Learning con Scikit-learn (Decision Tree)

## Otras herramientas

- Pandas
- OpenPyXL
- ReportLab

---

# ✨ Funcionalidades principales

- 🔐 Registro e inicio de sesión mediante Firebase Authentication.
- 💬 Chatbot médico impulsado por inteligencia artificial.
- 👤 Gestión de perfiles médicos personalizados.
- 📊 Monitoreo básico de signos vitales mediante Machine Learning.
- 📝 Historial de conversaciones por usuario.
- 📄 Generación de reportes en PDF.
- 🤖 Respuestas personalizadas utilizando el contexto médico del usuario.

---

# 🏗️ Arquitectura general

```text
                 React + Vite
                       │
                 HTTP (REST API)
                       │
                       ▼
                 Flask (Backend)
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
 Chatbot IA      Monitoreo ML     Reportes PDF
        │
        ▼
 Gemma 3 (OpenRouter)
        │
        ▼
 Firebase Authentication
        │
        ▼
 Cloud Firestore
```

---

# 📁 Estructura del proyecto

```text
PROYECTO/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   ├── firebase.js
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── templates/
│   ├── chat.html
│   ├── index.html
│   └── usuarios.html
│
├── app.py
├── asistente.py
├── ollama_modelo.py
├── reporte.py
├── datos_salud.csv
├── historial_salud.csv
├── requirements.txt
├── .env.example
└── README.md
```

## Archivos principales

| Archivo | Descripción |
|----------|-------------|
| `app.py` | Punto de entrada del backend y definición de las rutas de la API. |
| `asistente.py` | Lógica principal del asistente médico. |
| `ollama_modelo.py` | Comunicación con el modelo de lenguaje utilizado por el chatbot. |
| `reporte.py` | Generación de reportes en PDF. |
| `frontend/` | Aplicación desarrollada con React y Vite. |

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/USUARIO/NOMBRE-REPOSITORIO.git
```

```bash
cd NOMBRE-REPOSITORIO
```

---

## 2. Instalar dependencias del backend

Se recomienda utilizar un entorno virtual.

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## 3. Instalar dependencias del frontend

```bash
cd frontend

npm install
```

---

# 🔑 Variables de entorno

El proyecto utiliza archivos `.env` para almacenar información sensible.

Por motivos de seguridad, estos archivos **no se incluyen** en el repositorio.

Se deben crear utilizando los archivos de ejemplo correspondientes.

## Backend

Crear un archivo:

```text
.env
```

Ejemplo:

```env
OPENROUTER_API_KEY=TU_API_KEY
```

---

## Frontend

Crear un archivo:

```text
frontend/.env
```

Ejemplo:

```env
VITE_FIREBASE_API_KEY=
VITE_FIREBASE_AUTH_DOMAIN=
VITE_FIREBASE_PROJECT_ID=
VITE_FIREBASE_STORAGE_BUCKET=
VITE_FIREBASE_MESSAGING_SENDER_ID=
VITE_FIREBASE_APP_ID=
```

> Las credenciales de Firebase y la API Key deben ser proporcionadas por el responsable del proyecto.

---

# ▶️ Ejecutar el proyecto

## Backend

Desde la carpeta raíz:

```bash
python app.py
```

---

## Frontend

Desde la carpeta `frontend`:

```bash
npm run dev
```

---

Una vez iniciado el proyecto:

- Frontend: `http://localhost:5173`
- Backend: `http://localhost:5000`

---

# 🤝 Notas para colaboradores

- Mantener los archivos `.env` fuera del repositorio.
- No compartir credenciales mediante GitHub.
- Instalar las dependencias antes de ejecutar el proyecto.
- Mantener actualizados `requirements.txt` y `package.json` cuando se agreguen nuevas dependencias.
- Coordinar cualquier cambio relacionado con la lógica del asistente médico para evitar conflictos en el desarrollo.

---

# 📌 Consideraciones

- El asistente proporciona orientación básica basada en inteligencia artificial.
- El modelo de Machine Learning analiza temperatura corporal, frecuencia cardíaca y presión sistólica para identificar posibles estados de alerta.
- Las respuestas del chatbot se personalizan utilizando la información registrada en el perfil médico del usuario.
- El proyecto tiene fines académicos y de aprendizaje, por lo que no debe utilizarse como herramienta de diagnóstico médico profesional.
