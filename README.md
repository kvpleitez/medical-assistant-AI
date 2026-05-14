# Asistente Médico con Inteligencia Artificial

Proyecto desarrollado con Python, Flask, React y Firebase enfocado en asistencia médica inteligente, monitoreo de salud y experiencia personalizada para cada usuario.

## Descripción del proyecto

Este proyecto consiste en un asistente médico impulsado por inteligencia artificial capaz de:

* Analizar síntomas mediante IA
* Mantener conversaciones tipo chatbot
* Guardar historial de conversaciones por usuario
* Gestionar perfiles médicos personalizados
* Monitorear signos vitales
* Generar recomendaciones básicas de salud
* Personalizar respuestas según el perfil médico del paciente

El sistema fue desarrollado como proyecto académico para la materia de Inteligencia Artificial con Python.

---

# Tecnologías utilizadas

## Backend

* Python
* Flask
* Scikit-learn
* Ollama Cloud
* Pandas

## Frontend

* React
* Vite
* Tailwind CSS

## Base de datos y autenticación

* Firebase Authentication
* Cloud Firestore

## Modelo de Inteligencia Artificial

* Gemma 3 4B Cloud

---

# Funcionalidades principales

## Sistema de autenticación

* Registro de usuarios
* Inicio de sesión
* Gestión individual por usuario

## Chatbot médico con IA

* Conversaciones en tiempo real
* Respuestas estructuradas y fáciles de entender
* Tono humanizado y empático
* Explicaciones médicas simplificadas

## Historial de chats

* Chats independientes por usuario
* Persistencia de conversaciones en Firebase
* Creación de múltiples conversaciones

## Perfil médico inteligente

Cada usuario puede registrar:

* Nombre
* Edad
* Peso
* Altura
* Género
* Tipo de sangre
* Alergias
* Enfermedades crónicas
* Medicamentos frecuentes
* Contacto de emergencia

La IA utiliza esta información como contexto para personalizar las respuestas médicas.

## Monitoreo de signos vitales

El sistema analiza:

* Temperatura corporal
* Frecuencia cardíaca
* Presión sistólica

Mediante un modelo de Machine Learning utilizando DecisionTreeClassifier.

El sistema puede detectar:

* Estado normal
* Alerta media
* Alerta alta

Además, genera recomendaciones básicas según el resultado.

---

# Arquitectura general

Frontend desarrollado en React.

El frontend se comunica con Flask mediante API REST.

Flask procesa:

* Peticiones del chatbot
* Integración con IA
* Modelo de Machine Learning
* Procesamiento médico básico

Firebase se utiliza para:

* Autenticación
* Base de datos
* Historial de chats
* Perfiles médicos

---

# Estructura del proyecto

```bash
PROYECTO/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── firebase.js
│
├── templates/
│
├── usuarios/
│
├── app.py
├── asistente_salud.py
├── ollama_modelo.py
├── datos_salud.csv
└── historial_salud.csv
```

---

# Objetivo del proyecto

El objetivo principal del proyecto es combinar inteligencia artificial, análisis de datos y desarrollo web para crear un sistema médico básico que ayude a orientar a los usuarios de manera más personalizada y accesible.

También busca demostrar cómo la IA puede integrarse en soluciones enfocadas en salud digital y experiencia de usuario.

---

# Enfoque del sistema

El proyecto integra distintas tecnologías para construir una experiencia médica inteligente y personalizada.

## React

Se utiliza para desarrollar la interfaz visual del sistema, permitiendo una experiencia moderna, dinámica e interactiva para el usuario.

## Flask y Python

Se encargan de la lógica principal del sistema, procesamiento de datos, comunicación con la inteligencia artificial y funcionamiento del monitoreo médico.

## Firebase

Permite gestionar:

* autenticación de usuarios
* almacenamiento de perfiles médicos
* historial de chats
* persistencia de información

## Machine Learning

Se implementa un modelo de clasificación utilizando DecisionTreeClassifier para analizar signos vitales y detectar posibles estados de alerta.

## Ollama + Gemma 3

El chatbot médico utiliza un modelo de inteligencia artificial capaz de interpretar síntomas y responder de manera personalizada, empática y fácil de entender.

---

# Autora

Karla Pleitez

Estudiante de Ingeniería en Inteligencia Artificial y Robótica.

Interesada en desarrollar soluciones tecnológicas con impacto social, salud digital e innovación basada en IA.
