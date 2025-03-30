<template>
  <div class="container">
    <h1>Buscar Operadora</h1>
    <input v-model="termo" @input="buscarOperadora" placeholder="Digite o nome da operadora..." />
    <ul v-if="resultados.length">
      <li v-for="operadora in resultados" :key="operadora.Registro_ANS">
        {{ operadora.Cidade }}
      </li>
    </ul>
    <p v-else>Nenhum resultado encontrado.</p>
    <pre>{{ resultados }}</pre>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      termo: '',
      resultados: []
    };
  },
  methods: {
    async buscarOperadora() {
      if (this.termo.length < 3) {
        this.resultados = [];
        return;
      }
      try {
        const response = await axios.get(`http://127.0.0.1:5000/buscar?termo=${this.termo}`);
        console.log("Dados recebidos:", response.data);
        this.resultados = response.data;
      } catch (error) {
        console.error("Erro ao buscar operadora", error);
      }
    }
  }
};
</script>

<style>
.container {
  text-align: center;
  margin: 20px;
}
input {
  padding: 10px;
  width: 300px;
  margin-bottom: 10px;
}
ul {
  list-style: none;
  padding: 0;
}
</style>
