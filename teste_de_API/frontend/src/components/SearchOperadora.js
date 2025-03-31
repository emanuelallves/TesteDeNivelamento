import axios from "axios";

export default async function buscarOperadora(termo) {
  if (termo.length < 3) {
    return [];
  }

  try {
    const response = await axios.get(`http://127.0.0.1:5000/buscar?termo=${termo}`);
    console.log("Dados recebidos:", response.data);
    return response.data;
  } catch (error) {
    console.error("Erro ao buscar operadora", error);
    return [];
  }
}
