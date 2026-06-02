import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/login";
import Register from "./pages/register";
import Home from "./pages/home";
import Chatbot from "./pages/chatbot";
import Monitor from "./pages/monitor";
import Profile from "./pages/profile";
import Historial from "./pages/historial";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Login />} />

        <Route path="/register" element={<Register />} />

        <Route path="/home" element={<Home />} />

        <Route path="/chatbot" element={<Chatbot />} />

        <Route path="/monitor" element={<Monitor />} />

        <Route path="/profile" element={<Profile />} />

        <Route path="/historial" element={<Historial />} />

      </Routes>

    </BrowserRouter>
  );
}

export default App;