import { useState } from "react";

import Sidebar from "../components/Sidebar";

function Monitor() {

  const [abierto, setAbierto] = useState(false);

  const [temperatura, setTemperatura] = useState("");

  const [frecuencia, setFrecuencia] = useState("");

  const [presion, setPresion] = useState("");

  const [resultado, setResultado] = useState(null);

  const analizar = async () => {

    const response = await fetch(
      "http://127.0.0.1:5000/api/monitor",
      {

        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify({

          temperatura,

          frecuencia,

          presion
        })
      }
    );

    const data = await response.json();

    setResultado(data);
  };

  const colorEstado = () => {

    if (!resultado) return "bg-white";

    if (resultado.estado === "normal") {
      return "bg-green-100";
    }

    if (resultado.estado === "alerta_media") {
      return "bg-yellow-100";
    }

    return "bg-red-100";
  };

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

        <h1 className="text-3xl font-bold ml-4">
          Monitoreo Médico
        </h1>

      </div>

      {/* Contenido */}
      <div className="p-10 max-w-4xl mx-auto">

        <div className="bg-white rounded-2xl shadow-lg p-10">

          <h2 className="text-2xl font-bold mb-6">
            Ingresar signos vitales
          </h2>

          <div className="grid md:grid-cols-3 gap-6">

            <input
              type="number"
              placeholder="Temperatura"
              value={temperatura}
              onChange={(e) =>
                setTemperatura(e.target.value)
              }
              className="border p-4 rounded-xl"
            />

            <input
              type="number"
              placeholder="Frecuencia cardíaca"
              value={frecuencia}
              onChange={(e) =>
                setFrecuencia(e.target.value)
              }
              className="border p-4 rounded-xl"
            />

            <input
              type="number"
              placeholder="Presión sistólica"
              value={presion}
              onChange={(e) =>
                setPresion(e.target.value)
              }
              className="border p-4 rounded-xl"
            />

          </div>

          <button
            onClick={analizar}
            className="bg-blue-600 text-white px-8 py-4 rounded-xl mt-8"
          >
            Analizar estado de salud
          </button>

        </div>

        {/* Resultado */}
        {resultado && (

          <div
            className={`${colorEstado()} rounded-2xl shadow-lg p-10 mt-10`}
          >

            <h2 className="text-3xl font-bold mb-6">

              Estado:
              {" "}
              {resultado.estado}

            </h2>

            <div className="mb-6">

              <h3 className="text-xl font-bold mb-3">
                Recomendaciones:
              </h3>

              <ul className="list-disc ml-6">

                {resultado.recomendaciones.map(
                  (rec, index) => (

                    <li key={index}>
                      {rec}
                    </li>
                  )
                )}

              </ul>

            </div>

            <div>

              <h3 className="text-xl font-bold">
                Variable más influyente:
              </h3>

              <p className="mt-2">
                {resultado.variable_importante}
              </p>

            </div>

          </div>

        )}

      </div>

    </div>
  );
}

export default Monitor;