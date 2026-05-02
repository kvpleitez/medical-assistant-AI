import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/login";
import Register from "./pages/register";
import Home from "./pages/home";
import Chatbot from "./pages/chatbot";
import Monitor from "./pages/monitor";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Login />} />

        <Route path="/register" element={<Register />} />

        <Route path="/home" element={<Home />} />

        <Route path="/chatbot" element={<Chatbot />} />

        <Route path="/monitor" element={<Monitor />} />

      </Routes>

    </BrowserRouter>
  );
}

export default App;