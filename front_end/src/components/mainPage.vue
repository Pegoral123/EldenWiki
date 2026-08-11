<template>
  <!-- Página principal que combina Navbar, seção de locais e Footer -->
  <Navbar />
  <div
    class="hero"
    :style="{ backgroundImage: `url(${require('@/assets/fundo_2.webp')})` }"
  >
    <LocationsSection />
  </div>
  <Footer />
</template>

<script setup>
// Componentes compostos usados nesta página
import Navbar from "@/components/navBar.vue";
import Footer from "@/components/footerPage.vue";
import LocationsSection from "@/components/locationsSection.vue";

/*
  mainPage.vue é um wrapper simples que monta a página principal do app.
  Mantemos a maioria das responsabilidades de exibição em `LocationsSection`.
*/
</script>

<style scoped>
.hero {
  position: relative;
  width: 100%;
  min-height: 100vh;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed; /* efeito parallax */
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  text-align: center;
  font-family: serif;
}
</style>
