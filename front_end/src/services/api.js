import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export function setAuthToken(token) {
  if (token) {
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  } else {
    delete api.defaults.headers.common["Authorization"];
  }
}

export async function Limgrave_bosses() {
  try {
    const resposta = await api.get("/boss/limgrave_bosses");
    return resposta.data;
  } catch (erro) {
    console.error("Erro ao buscar bosses de Limgrave:", erro);
    throw erro;
  }
}

export async function caelid_bosses() {
  try {
    const resposta = await api.get("/boss/caelid_bosses");
    return resposta.data;
  } catch (erro) {
    console.error("Erro ao buscar bosses de Caelid:", erro);
    throw erro;
  }
}

export async function RotaLimgrave() {
  try {
    const resposta = await api.get("/locations/limgrave");
    return resposta.data;
  } catch (erro) {
    console.error("Erro ao buscar local Limgrave:", erro);
    throw erro;
  }
}

export async function RotaCaelid() {
  try {
    const resposta = await api.get("/locations/caelid");
    return resposta.data;
  } catch (erro) {
    console.error("Erro ao buscar local Caelid:", erro);
    throw erro;
  }
}

export async function loginUser(email, password) {
  try {
    const resposta = await api.post("/auth/login", { email, password });
    return resposta.data;
  } catch (erro) {
    if (erro.response && erro.response.data) throw erro.response.data;
    throw erro;
  }
}

export async function registerUser(name, email, password) {
  try {
    const resposta = await api.post("/auth/register", {
      name,
      email,
      password,
    });
    return resposta.data;
  } catch (erro) {
    if (erro.response && erro.response.data) throw erro.response.data;
    throw erro;
  }
}
