import { useState, useEffect } from "react";

import { v4 as uuidv4 } from "uuid";

import { Link } from "react-router-dom";

import { db, auth } from "../firebase";

import {
  collection,
  addDoc,
  getDocs,
  query,
  orderBy,
  doc,
  setDoc,
  getDoc
} from "firebase/firestore";

import Sidebar from "../components/Sidebar";

function Chatbot() {

  const [abierto, setAbierto] = useState(false);

  const [mensaje, setMensaje] = useState("");

  const [mensajes, setMensajes] = useState([]);

  const [chats, setChats] = useState([]);

  const [chatActual, setChatActual] = useState(null);

  const [perfilUsuario, setPerfilUsuario] = useState(null);

  if (!auth.currentUser) {
    return (
      <div className="p-10">
        Debes iniciar sesión
      </div>
    );
  }

  // Cargar chats al iniciar
  useEffect(() => {
    cargarChats();
    cargarPerfil();
  }, []);

  const cargarChats = async () => {

    const q = query(
      collection(
        db,
        "usuarios",
        auth.currentUser.uid,
        "chats"
      ),
      orderBy("fecha", "desc")
    );

    const querySnapshot = await getDocs(q);

    const chatsFirebase = [];

    querySnapshot.forEach((doc) => {

      chatsFirebase.push({
        id: doc.id,
        ...doc.data()
      });
    });

    setChats(chatsFirebase);
  };

  //Abrir un chat existente
  const abrirChat = (chat) => {
    setChatActual(chat.chatId);
    setMensajes(chat.mensajes || []);
  };

  // Crear nuevo chat
  const nuevoChat = () => {

    setMensajes([]);

    setChatActual(uuidv4());
  };

  // Enviar mensaje
  const enviarMensaje = async () => {

    if (!mensaje.trim()) return;

    let idChat = chatActual;

    // Si no existe chat, crear uno nuevo
    if (!idChat) {

      idChat = uuidv4();

      setChatActual(idChat);
    }

    const nuevoMensajeUsuario = {
      tipo: "usuario",
      texto: mensaje,
      fecha: new Date().toLocaleString()
    };

    setMensajes(prev => [
      ...prev,
      nuevoMensajeUsuario
    ]);

    const response = await fetch(
      "http://127.0.0.1:5000/api/chat",
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify({
          mensaje: mensaje,
          perfil: perfilUsuario
        })
      }
    );

    const data = await response.json();

    const nuevoMensajeIA = {
      tipo: "ia",
      texto: data.respuesta,
      fecha: new Date().toLocaleString()
    };

    setMensajes(prev => [
      ...prev,
      nuevoMensajeIA
    ]);

    // Guardar en Firebase
    await setDoc(
      doc(
        db,
        "usuarios",
        auth.currentUser.uid,
        "chats",
        idChat
      ),
      {

        chatId: idChat,

        titulo: mensaje.substring(0, 30),

        mensajes: [
          ...mensajes,
          nuevoMensajeUsuario,
          nuevoMensajeIA
        ],

        fecha: new Date()
      }
    );

    cargarChats();

    const abrirChat = (chat) => {
      setChatActual(chat.chatId);
      setMensajes(chat.mensajes || []);
    };

    setMensaje("");
  };

    const cargarPerfil = async () => {

      const ref = doc(
        db,
        "usuarios",
        auth.currentUser.uid
      );

      const snap = await getDoc(ref);

      if (snap.exists()) {

        setPerfilUsuario(
          snap.data().perfil
        );
      }
    };

  return (

    <div className="flex bg-gray-100 h-screen overflow-hidden">
      <Sidebar 
        abierto={abierto}
        setAbierto={setAbierto}
      />

      {/* Sidebar */}
      <div className="w-80 bg-white shadow-lg p-4 h-full overflow-y-auto">

        <button
          onClick={nuevoChat}
          className="w-full bg-blue-600 text-white p-4 rounded-xl mb-6"
        >
          + Nuevo Chat
        </button>

        <div className="space-y-3">

          {chats.map((chat, index) => (

        <div
          key={index}
          onClick={() => abrirChat(chat)}
          className="bg-gray-100 p-4 rounded-xl cursor-pointer hover:bg-gray-200"
        >
          {chat.titulo}
        </div>

    ))}

        </div>

      </div>

      {/* Chat principal */}
      <div className="flex-1 flex flex-col h-screen">

        <div className="bg-white shadow p-4 flex items-center sticky top-0 z-10">
          <button
            onClick={() => setAbierto(true)}
            className="text-3xl"
          >
            ☰
          </button>

          <h1 className="text-3xl font-bold ml-4">
            Chatbot Médico IA
          </h1>

        </div>

        <div className="flex-1 overflow-y-auto p-6">

          <div className="max-w-4xl mx-auto space-y-4">

            {mensajes.map((msg, index) => (

              <div
                key={index}
                className={`p-4 rounded-2xl max-w-xl ${
                  msg.tipo === "usuario"
                    ? "bg-blue-600 text-white ml-auto"
                    : "bg-white shadow"
                }`}
              >
                <p 
                className="leading-relaxed"
                style={{ whiteSpace: "pre-line" }}>
                <div>
                  <p className="whitespace-pre-line">
                    {msg.texto}
                  </p>

                  <p className="text-xs text-gray-400 mt-2 text-right">
                    {msg.fecha}
                  </p>
                </div>

                </p>
              </div>

            ))}

          </div>

        </div>

        <div className="bg-white p-4 shadow">

          <div className="max-w-4xl mx-auto flex gap-4">

            <input
              type="text"
              placeholder="Describe tus síntomas..."
              value={mensaje}
              onChange={(e) => setMensaje(e.target.value)}
              className="flex-1 border rounded-xl p-4"
            />

            <button
              onClick={enviarMensaje}
              className="bg-blue-600 text-white px-6 rounded-xl"
            >
              Enviar
            </button>

          </div>

        </div>

      </div>

    </div>
  );
}

export default Chatbot;