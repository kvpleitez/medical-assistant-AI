import { Link, useNavigate } from "react-router-dom";

import { signOut } from "firebase/auth";

import { auth } from "../firebase";

function Sidebar({ abierto, setAbierto }) {

  const navigate = useNavigate();

  const cerrarSesion = async () => {

    await signOut(auth);

    navigate("/");
  };

  return (

    <>
      {/* Fondo oscuro */}
      {abierto && (

        <div
          className="fixed inset-0 bg-black/40 z-40"
          onClick={() => setAbierto(false)}
        />

      )}

      {/* Sidebar */}
      <div
        className={`
          fixed top-0 left-0 h-full w-64 bg-white shadow-lg p-6 z-50
          transform transition-transform duration-300

          ${abierto ? "translate-x-0" : "-translate-x-full"}
        `}
      >

        <h1 className="text-2xl font-bold mb-10">
          Asistente Médico IA
        </h1>

        <div className="flex flex-col gap-4">

          <Link
            to="/home"
            onClick={() => setAbierto(false)}
            className="bg-gray-100 p-4 rounded-xl hover:bg-gray-200 transition"
          >
            🏠 Inicio
          </Link>

          <Link
            to="/chatbot"
            onClick={() => setAbierto(false)}
            className="bg-gray-100 p-4 rounded-xl hover:bg-gray-200 transition"
          >
            💬 Chatbot
          </Link>

          <Link
            to="/monitor"
            onClick={() => setAbierto(false)}
            className="bg-gray-100 p-4 rounded-xl hover:bg-gray-200 transition"
          >
            📈 Monitoreo
          </Link>

          <button
            onClick={cerrarSesion}
            className="bg-red-500 text-white p-4 rounded-xl hover:bg-red-600 transition mt-10"
          >
            🚪 Cerrar sesión
          </button>

        </div>

      </div>

    </>
  );
}

export default Sidebar;