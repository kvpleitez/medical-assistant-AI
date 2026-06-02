import { useEffect, useState } from "react";

import { db, auth } from "../firebase";

import {
  collection,
  getDocs,
  query,
  orderBy,
  doc,
  getDoc
} from "firebase/firestore";

import Sidebar from "../components/Sidebar";

function Historial() {

  const [consultas, setConsultas] = useState([]);

  const [perfil, setPerfil] = useState({});

  const [abierto, setAbierto] = useState(false);

  const [reporte, setReporte] = useState("");

  const [consultasSeleccionadas, setConsultasSeleccionadas] = useState([]);

  useEffect(() => {

    cargarConsultas();
    cargarPerfil();

  }, []);

  const cargarConsultas = async () => {

    const q = query(
      collection(
        db,
        "usuarios",
        auth.currentUser.uid,
        "consultas"
      ),
      orderBy("fecha", "desc")
    );

    const querySnapshot = await getDocs(q);

    const lista = [];

    querySnapshot.forEach((doc) => {

      lista.push(doc.data());

    });

    setConsultas(lista);
  };

    const cargarPerfil = async () => {

      const docRef = doc(
        db,
        "usuarios",
        auth.currentUser.uid
      );

      const docSnap = await getDoc(docRef);

      if (docSnap.exists()) {

        setPerfil(
          docSnap.data().perfil || {}
        );

      }
    };

  const generarReporte = async () => {

    const response = await fetch(
        "http://127.0.0.1:5000/api/reporte",
        {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            historial: consultas
        })
        }
    );

    const data = await response.json();

    setReporte(data.reporte);
  };

    const generarPDF = async () => {

    const response = await fetch(
        "http://127.0.0.1:5000/api/reporte-pdf",
        {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            consultas: consultasSeleccionadas,
            perfil: perfil
        })
        }
    );

    const blob = await response.blob();

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "reporte_clinico.pdf";

    a.click();
    };

    const seleccionarConsulta = (consulta) => {

    const yaExiste = consultasSeleccionadas.includes(consulta);

    if (yaExiste) {

        setConsultasSeleccionadas(
        consultasSeleccionadas.filter(
            c => c !== consulta
        )
        );

    } else {

        setConsultasSeleccionadas([
        ...consultasSeleccionadas,
        consulta
        ]);
    }
    };

  return (

    <div className="flex bg-gray-100 h-screen overflow-hidden">

      <Sidebar
        abierto={abierto}
        setAbierto={setAbierto}
      />

      <div className="flex-1 flex flex-col">

        <div className="bg-white shadow p-4 flex items-center sticky top-0 z-10">

          <button
            onClick={() => setAbierto(true)}
            className="text-3xl"
          >
            ☰
          </button>

          <h1 className="text-3xl font-bold ml-4">
            Historial Médico
          </h1>

          <button
            onClick={generarReporte}
            className="ml-auto bg-blue-600 text-white px-4 py-2 rounded-xl"
          >
            Generar Reporte IA
          </button>

          <button
            onClick={generarPDF}
            className="ml-4 bg-green-600 text-white px-4 py-2 rounded-xl"
          >
            Generar PDF Clínico
          </button>

        </div>

        <div className="flex-1 overflow-y-auto p-6">

          <div className="max-w-4xl mx-auto space-y-6">

            {reporte && (

            <div className="bg-blue-50 p-6 rounded-2xl shadow mb-6">

                <h2 className="text-2xl font-bold mb-4">
                Reporte Inteligente
                </h2>

                <p className="whitespace-pre-line">
                {reporte}
                </p>

            </div>

            )}

            {consultas.map((consulta, index) => (

              <div
                key={index}
                className={`p-6 rounded-2xl shadow border-2 ${
                    consultasSeleccionadas.includes(consulta)
                    ? "border-blue-500 bg-blue-50"
                    : "bg-white border-transparent"
                }`}
              >

                <p className="text-sm text-gray-500 mb-4">
                  {new Date(
                    consulta.fecha.seconds * 1000
                  ).toLocaleString()}
                </p>

                <button
                    onClick={() => seleccionarConsulta(consulta)}
                    className="mb-4 bg-blue-600 text-white px-4 py-2 rounded-xl"
                >
                    {
                        consultasSeleccionadas.includes(consulta)
                        ? "Deseleccionar"
                        : "Seleccionar"
                    }
                </button>

                <h2 className="font-bold text-lg mb-2">
                  Consulta realizada
                </h2>

                <p className="mb-6">
                  {consulta.sintomas}
                </p>

                <h2 className="font-bold text-lg mb-2">
                  Respuesta de la IA
                </h2>

                <p className="whitespace-pre-line">
                  {consulta.respuestaIA}
                </p>

              </div>

            ))}

          </div>

        </div>

      </div>

    </div>
  );
}

export default Historial;