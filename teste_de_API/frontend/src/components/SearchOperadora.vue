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
import buscarOperadora from "./SearchOperadora.js";

export default {
  data() {
    return {
      termo: "",
      resultados: [],
    };
  },
  methods: {
    async buscarOperadora() {
      this.resultados = await buscarOperadora(this.termo);
    },
  },
};
</script>

<style src="./SearchOperadora.css"></style>
