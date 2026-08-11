<template>
  <div class="hero" :style="{ backgroundImage: `url(${fundo})` }">
    <div class="overlay"></div>
    <div class="conteudo-central">
      <img :src="titulo" alt="Título" class="titulo-img" />
      <router-link to="/mainPage" class="btn btn-dark btn-journey">
        Iniciar jornada
      </router-link>
    </div>
  </div>
</template>

<script setup>
import tituloImg from "@/assets/TITULO_ELDEN_WIKI.png";
import fundoImg from "@/assets/fundo_3.webp";

const titulo = tituloImg;
const fundo = fundoImg;
</script>

<style>
html,
body {
  height: 100%;
  margin: 0;
}
</style>

<style scoped>
.hero {
  position: relative;
  width: 100%;
  min-height: 100vh;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  text-align: center;
  font-family: serif;
  color: #d8b868;
}

.overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  pointer-events: none;
}

.conteudo-central {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.25rem;
  padding: 0 1rem;
  max-width: 900px;
  width: 100%;
}

.titulo-img {
  max-width: 450px;
  width: 100%;
  height: auto;
  display: block;
}

.btn-journey {
  padding: 0.75rem 1.5rem;
  font-size: 0.95rem;
  border-radius: 6px;
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.15s ease;
}

.btn-journey:hover {
  transform: scale(1.04);
}
</style>
