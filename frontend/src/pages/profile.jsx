import { useState, useEffect } from "react";

import { auth, db } from "../firebase";

import {
  doc,
  getDoc,
  setDoc
} from "firebase/firestore";

import Sidebar from "../components/Sidebar";

function Profile() {

    const [abierto, setAbierto] = useState(false);

    const [perfil, setPerfil] = useState({
    nombre: "",
    edad: "",
    peso: "",
    altura: "",
    genero: "",
    sangre: "",

    sinAlergias: false,
    alergias: "",

    sinEnfermedades: false,
    enfermedades: "",

    sinMedicamentos: false,
    medicamentos: "",

    codigoPais: "+503",
    emergencia: ""
    });

  useEffect(() => {
    cargarPerfil();
  }, []);

  const cargarPerfil = async () => {

    const ref = doc(
      db,
      "usuarios",
      auth.currentUser.uid
    );

    const snap = await getDoc(ref);

    if (snap.exists()) {

      setPerfil({
        ...perfil,
        ...snap.data().perfil
      });
    }
  };

  const guardarPerfil = async () => {

    await setDoc(
      doc(
        db,
        "usuarios",
        auth.currentUser.uid
      ),
      {
        perfil: perfil
      },
      { merge: true }
    );

    alert("Perfil guardado");
  };

  return (

    <div className="flex min-h-screen bg-gray-100">

      <Sidebar
        abierto={abierto}
        setAbierto={setAbierto}
      />

      <div className="flex-1 p-10">

        <button
          onClick={() => setAbierto(true)}
          className="text-3xl mb-6"
        >
          ☰
        </button>

        <div className="bg-white p-10 rounded-2xl shadow max-w-3xl">

          <h1 className="text-3xl font-bold mb-8">
            Perfil Médico
          </h1>

          <div className="grid grid-cols-2 gap-4">

    {/* Nombre */}
            <input
              placeholder="Nombre"
              value={perfil.nombre}
              onChange={(e) =>
                setPerfil({
                  ...perfil,
                  nombre: e.target.value
                })
              }
              className="border p-4 rounded-xl"
            />

{/* Edad */}
            <input
                type="number"
                min="18"
                max="120"
                placeholder="Edad"
                value={perfil.edad}
                onChange={(e) =>
                    setPerfil({
                    ...perfil,
                    edad: e.target.value
                    })
                }
                className="border p-4 rounded-xl"
            />

{/* Peso */}
            <input
                type="number"
                placeholder="Peso (libras)"
                value={perfil.peso}
                onChange={(e) =>
                    setPerfil({
                    ...perfil,
                    peso: e.target.value
                    })
                }
                className="border p-4 rounded-xl"
            />

{/* Altura */}
            <input
            type="number"
            placeholder="Altura (cm)"
            value={perfil.altura}
            onChange={(e) =>
                setPerfil({
                ...perfil,
                altura: e.target.value
                })
            }
            className="border p-4 rounded-xl"
            />

{/* Genero */}
            <select
                value={perfil.genero}
                onChange={(e) =>
                    setPerfil({
                    ...perfil,
                    genero: e.target.value
                    })
                }
                className="border p-4 rounded-xl"
                >

                <option value="">
                    Seleccione género
                </option>

                <option value="Femenino">
                    Femenino
                </option>

                <option value="Masculino">
                    Masculino
                </option>

                <option value="Otro">
                    Otro
                </option>

                <option value="Prefiero no decirlo">
                    Prefiero no decirlo
                </option>

            </select>

{/* Tipo de sangre */}
            <input
              placeholder="Tipo de sangre"
              value={perfil.sangre}
              onChange={(e) =>
                setPerfil({
                  ...perfil,
                  sangre: e.target.value
                })
              }
              className="border p-4 rounded-xl"
            />

{/* Apartado alergias */}
        </div>

            <div className="mt-4">

            <label className="flex items-center gap-2 mb-2">

                <input
                type="checkbox"
                checked={perfil.sinAlergias}
                onChange={(e) =>
                    setPerfil({
                    ...perfil,
                    sinAlergias: e.target.checked
                    })
                }
                />

                Ninguna alergia

            </label>

            {!perfil.sinAlergias && (

                <textarea
                placeholder="Alergias"
                value={perfil.alergias}
                onChange={(e) =>
                    setPerfil({
                    ...perfil,
                    alergias: e.target.value
                    })
                }
                className="border p-4 rounded-xl w-full"
                />

            )}

        </div>

{/* Apartado enfermedades cronicas */}
        <div className="mt-4">

        <label className="flex items-center gap-2 mb-2">

            <input
            type="checkbox"
            checked={perfil.sinEnfermedades}
            onChange={(e) =>
                setPerfil({
                ...perfil,
                sinEnfermedades: e.target.checked
                })
            }
            />

            Ninguna enfermedad crónica

        </label>

        {!perfil.sinEnfermedades && (

            <textarea
            placeholder="Enfermedades crónicas"
            value={perfil.enfermedades}
            onChange={(e) =>
                setPerfil({
                ...perfil,
                enfermedades: e.target.value
                })
            }
            className="border p-4 rounded-xl w-full"
            />

        )}

        </div>

{/* Apartado Medicamentos */}
        <div className="mt-4">

        <label className="flex items-center gap-2 mb-2">

            <input
            type="checkbox"
            checked={perfil.sinMedicamentos}
            onChange={(e) =>
                setPerfil({
                ...perfil,
                sinMedicamentos: e.target.checked
                })
            }
            />

            Ningún medicamento frecuente

        </label>

        {!perfil.sinMedicamentos && (

            <textarea
            placeholder="Medicamentos"
            value={perfil.medicamentos}
            onChange={(e) =>
                setPerfil({
                ...perfil,
                medicamentos: e.target.value
                })
            }
            className="border p-4 rounded-xl w-full"
            />

        )}

        </div>
            <div className="flex gap-2 mt-4">

            <select
                value={perfil.codigoPais}
                onChange={(e) =>
                setPerfil({
                    ...perfil,
                    codigoPais: e.target.value
                })
                }
                className="border p-4 rounded-xl"
            >

                <option value="+503">+503</option>
                <option value="+502">+502</option>
                <option value="+504">+504</option>
                <option value="+505">+505</option>
                <option value="+1">+1</option>

            </select>

            <input
                type="tel"
                placeholder="Teléfono de emergencia"
                value={perfil.emergencia}
                onChange={(e) =>
                setPerfil({
                    ...perfil,
                    emergencia: e.target.value
                })
                }
                className="border p-4 rounded-xl flex-1"
            />

            </div>
          <button
            onClick={guardarPerfil}
            className="bg-blue-600 text-white px-8 py-4 rounded-xl mt-6"
          >
            Guardar Perfil
          </button>

        </div>

      </div>

    </div>
  );
}

export default Profile;