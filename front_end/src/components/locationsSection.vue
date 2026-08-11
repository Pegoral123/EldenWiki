<template>
  <!--
    Componente de exibição de locais e bosses (seções de jogo).
    Estados possíveis (status): 'loading', 'error', 'success'.
    - loading: mostra spinner
    - error: mostra modal com botão de retry
    - success: renderiza dados de locais e listas de bosses
  -->
  <section class="locais-container">
    <div v-if="status === 'loading'" class="loading-state">
      <div class="spinner" aria-hidden="true"></div>
      <p>Carregando informações... Aguarde.</p>
    </div>

    <div v-else-if="status === 'error'" class="modal-state">
      <div class="modal-box">
        <div class="error-state">
          <p>⚠️ Erro ao carregar os dados!</p>
          <p>{{ errorMessage }}</p>
          <button @click="fetchData" class="retry-btn">Tentar Novamente</button>
        </div>
      </div>
    </div>

    <div v-else-if="status === 'success'">
      <section v-if="limgrave_local && limgrave_local.Local">
        <h1 class="locais-title">{{ limgrave_local.Local }}</h1>
        <h2 class="locais-subtitle">{{ limgrave_local.SubTitulo }}</h2>
        <img
          :src="require('@/assets/limgrave_img.webp')"
          alt="Imagem de Limgrave"
          class="locais_img"
        />
        <div class="locais-desc">
          <p>{{ limgrave_local.Descricao }}</p>
        </div>

        <div class="bosses-container" v-if="(bosses_limgrave || []).length">
          <div
            class="boss-card"
            v-for="boss in bosses_limgrave || []"
            :key="boss.id"
          >
            <h1 class="boss-title">{{ boss.name }}</h1>
            <h2 class="boss-location">{{ boss.location }}</h2>
            <img
              :src="boss.image"
              :alt="`Imagem do boss ${boss.name}`"
              class="boss-img"
            />
            <div class="boss-desc">
              <p>{{ boss.description }}</p>
            </div>
            <div class="boss-stats">
              <p><strong>Saúde:</strong> {{ boss.Saúde }}</p>
              <p><strong>Defesa:</strong> {{ boss.Defesa }}</p>
              <p><strong>Postura:</strong> {{ boss.Postura }}</p>
              <p><strong>Resistência:</strong> {{ boss.Resistencia }}</p>
              <p><strong>Fraqueza:</strong> {{ boss.Fraqueza }}</p>
              <p><strong>Recompensa:</strong> {{ boss.Recompensa }}</p>
            </div>
          </div>
        </div>
      </section>

      <section v-if="caelid_local && caelid_local.Local">
        <h1 class="locais-title">{{ caelid_local.Local }}</h1>
        <h2 class="locais-subtitle">{{ caelid_local.SubTitulo }}</h2>
        <img
          :src="require('@/assets/caelid_img.webp')"
          alt="Imagem de Caelid"
          class="locais_img"
        />
        <div class="locais-desc">
          <p>{{ caelid_local.Descricao }}</p>
        </div>

        <div class="bosses-container" v-if="(bosses_caelid || []).length">
          <div
            class="boss-card"
            v-for="boss in bosses_caelid || []"
            :key="boss.id"
          >
            <h1 class="boss-title">{{ boss.name }}</h1>
            <h2 class="boss-location">{{ boss.location }}</h2>
            <img
              :src="boss.image"
              :alt="`Imagem do boss ${boss.name}`"
              class="boss-img"
            />
            <div class="boss-desc">
              <p>{{ boss.description }}</p>
            </div>
            <div class="boss-stats">
              <p><strong>Saúde:</strong> {{ boss.Saúde }}</p>
              <p><strong>Defesa:</strong> {{ boss.Defesa }}</p>
              <p><strong>Postura:</strong> {{ boss.Postura }}</p>
              <p><strong>Resistência:</strong> {{ boss.Resistencia }}</p>
              <p><strong>Fraqueza:</strong> {{ boss.Fraqueza }}</p>
              <p><strong>Recompensa:</strong> {{ boss.Recompensa }}</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  </section>
</template>

<script setup>
/*
  locationsSection.vue - script setup
  - importa rotas/serviços para obter dados de locais e bosses
  - gerencia estado reativo (refs): dados, status e mensagens de erro
  - exporta a função fetchData usada para retry
*/
import {
  RotaLimgrave,
  RotaCaelid,
  Limgrave_bosses,
  caelid_bosses,
} from "../services/api.js";
import { ref, onMounted } from "vue";

// dados reativos expostos ao template
const limgrave_local = ref({});
const caelid_local = ref({});
const bosses_limgrave = ref([]);
const bosses_caelid = ref([]);
// status: 'loading' | 'error' | 'success'
const status = ref("loading");
const errorMessage = ref("");

/**
 * Busca dados do backend para as seções de locais e bosses.
 * Usa Promise.all para paralelizar as requisições e reduzir tempo de carregamento.
 * Atualiza `status` para controlar a UI.
 */
async function fetchData() {
  status.value = "loading";
  errorMessage.value = "";

  try {
    const [lim, cae, bLim, bCae] = await Promise.all([
      RotaLimgrave(),
      RotaCaelid(),
      Limgrave_bosses(),
      caelid_bosses(),
    ]);

    // normaliza respostas nulas
    limgrave_local.value = lim || {};
    caelid_local.value = cae || {};
    bosses_limgrave.value = bLim || [];
    bosses_caelid.value = bCae || [];
    status.value = "success";
  } catch (err) {
    status.value = "error";
    errorMessage.value =
      "Houve um problema de comunicação com o servidor. Por favor, tente novamente.";
    console.error("Erro ao buscar dados:", err);
  }
}

// carregar dados ao montar o componente
onMounted(() => {
  fetchData();
});
</script>

<style scoped>
.locais-container {
  background: rgba(34, 34, 34, 0.75); /* Fundo escuro translúcido */
  border-radius: 18px;
  padding: 2.5rem;
  max-width: 1500px;
  margin: 3rem auto;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.45);
  color: #ffd700;
  text-align: center;
  position: relative; /* CRUCIAL para o posicionamento do modal de erro */
}

.locais-title {
  font-size: 3rem;
  font-weight: bold;
  color: #ffd700;
  text-shadow: 2px 2px 8px #000, 0 0 16px #222;
  margin-bottom: 0.5rem;
  text-align: center;
  letter-spacing: 2px;
}

.locais-subtitle {
  font-size: 1.7rem;
  color: #fffbe6;
  text-shadow: 1px 1px 6px #000;
  margin-bottom: 1.5rem;
  text-align: center;
  font-style: italic;
}

.locais-desc {
  font-size: 1.15rem;
  color: #f3e7b3;
  text-shadow: 1px 1px 4px #000;
  line-height: 1.7;
  margin-top: 0.5rem;
  white-space: pre-line;
}

.locais_img {
  margin-top: 1.5rem;
  max-width: 100%;
  max-height: 500px;
  width: auto;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
  display: block;
  object-fit: cover;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 2rem;
}

.bosses-container {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

.boss-card {
  background: rgba(34, 34, 34, 0.85);
  border-radius: 18px;
  padding: 2rem;
  width: 300px;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.45);
  color: #ffd700;
  text-align: left;
}

.boss-title {
  font-size: 1.8rem;
  font-weight: bold;
  color: #ffd700;
  text-shadow: 2px 2px 8px #000, 0 0 16px #222;
  margin-bottom: 1rem;
  text-align: center;
}

.boss-location {
  font-size: 1.2rem;
  color: #fffbe6;
  text-shadow: 1px 1px 6px #000;
  margin-bottom: 1rem;
  text-align: center;
}

.boss-img {
  max-width: 100%;
  max-height: 200px;
  width: auto;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
  display: block;
  margin: 1rem auto;
}

.boss-desc {
  font-size: 1rem;
  color: #f3e7b3;
  text-shadow: 1px 1px 4px #000;
  line-height: 1.5;
  margin-top: 1rem;
}

.boss-stats {
  margin-top: 1rem;
  font-size: 1rem;
}

/* Loading styles */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 1rem;
  min-height: 300px;
}

.spinner {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  border: 6px solid rgba(212, 175, 55, 0.2);
  border-top-color: #d4af37;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.modal-box {
  pointer-events: auto;
  position: relative;
  padding: 2.5rem;
  border-radius: 18px;
  width: 520px;
  max-width: 90%;

  color: #ffd700;
  text-align: center;
}
.error-state {
  color: #ffdddd;
  background: rgba(120, 20, 20, 0.6);
  padding: 1.5rem;
  border-radius: 12px;
  text-align: center;
}

.retry-btn {
  margin-top: 1rem;
  background: #efb810;
  color: #222;
  border: none;
  padding: 0.6rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.3s ease;
}

.retry-btn:hover {
  background: #ffc700;
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
}
</style>
