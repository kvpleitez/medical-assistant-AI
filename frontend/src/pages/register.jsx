import { useState } from "react";

import {
  createUserWithEmailAndPassword
} from "firebase/auth";

import { auth } from "../firebase";

import { useNavigate, Link } from "react-router-dom";

function Register() {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const registrar = async () => {

    try {

      await createUserWithEmailAndPassword(
        auth,
        email,
        password
      );

      alert("Usuario registrado correctamente");

      navigate("/");
x
    } catch (error) {

      alert(error.message);
    }
  };

  return (

    <div className="min-h-screen flex items-center justify-center bg-gray-100">

      <div className="bg-white p-10 rounded-2xl shadow-lg w-96">

        <h1 className="text-3xl font-bold mb-6 text-center">
          Crear Cuenta
        </h1>

        <input
          type="email"
          placeholder="Correo"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full border p-4 rounded-xl mb-4"
        />

        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full border p-4 rounded-xl mb-4"
        />

        <button
          onClick={registrar}
          className="w-full bg-blue-600 text-white p-4 rounded-xl"
        >
          Registrarse
        </button>

        <p className="mt-6 text-center">

          ¿Ya tienes cuenta?

          <Link
            to="/"
            className="text-blue-600 font-bold ml-2"
          >
            Inicia sesión
          </Link>

        </p>

      </div>

    </div>
  );
}

export default Register;