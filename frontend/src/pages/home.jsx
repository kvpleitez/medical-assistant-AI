import { Link } from "react-router-dom";
import { useState } from "react";
import Sidebar from "../components/Sidebar";

function Home() {
  const [abierto, setAbierto] = useState(false);
  return (
    <div className="bg-gray-100 min-h-screen">

      <Sidebar
        abierto={abierto}
        setAbierto={setAbierto}
      />

      {/* Barra superior */}
      <div className="bg-white shadow p-4 flex items-center">

        <button
          onClick={() => setAbierto(true)}
          className="text-3xl"
        >
          ☰
        </button>

        <h1 className="text-2xl font-bold ml-4">
          Asistente Médico IA
        </h1>

      </div>

      {/* Contenido */}
      <div className="p-10">

        <div className="grid md:grid-cols-2 gap-10 max-w-5xl mx-auto">

          <Link to="/monitor">

            <div className="bg-white rounded-2xl shadow-lg p-10 hover:scale-105 transition">

              <h2 className="text-3xl font-bold mb-4">
                Monitoreo Médico
              </h2>

              <p className="text-gray-600">
                Visualiza signos vitales y alertas médicas.
              </p>

            </div>

          </Link>

          <Link to="/chatbot">

            <div className="bg-white rounded-2xl shadow-lg p-10 hover:scale-105 transition">

              <h2 className="text-3xl font-bold mb-4">
                Chatbot IA
              </h2>

              <p className="text-gray-600">
                Consulta síntomas y recibe orientación médica básica.
              </p>

            </div>

          </Link>

        </div>

      </div>

    </div>
  );
}

export default Home;