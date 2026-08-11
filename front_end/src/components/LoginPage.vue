<template>
  <!-- Navbar global do site -->
  <Navbar />
  <div
    class="hero"
    :style="{ backgroundImage: `url(${require('@/assets/fundo_4.webp')})` }"
  >
    <div class="card">
      <div class="card-body">
        <h2 class="title">Login ao Reino das Sombras</h2>

        <form @submit.prevent="login" class="form">
          <div v-if="errorMessage" class="form-error">{{ errorMessage }}</div>
          <label class="input-wrap">
            <svg
              class="icon"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M12 12c2.761 0 5-2.239 5-5s-2.239-5-5-5-5 2.239-5 5 2.239 5 5 5z"
                stroke="#fff"
                stroke-width="1.2"
              />
              <path
                d="M4 20c0-4 4-6 8-6s8 2 8 6"
                stroke="#fff"
                stroke-width="1.2"
                stroke-linecap="round"
              />
            </svg>
            <input
              type="email"
              v-model="email"
              placeholder="Nome do Maculado (email)"
              autocomplete="email"
              aria-label="email"
            />
          </label>

          <label class="input-wrap">
            <svg
              class="icon"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <rect
                x="3"
                y="11"
                width="18"
                height="10"
                rx="2"
                stroke="#fff"
                stroke-width="1.2"
              />
              <path
                d="M7 11V8a5 5 0 0 1 10 0v3"
                stroke="#fff"
                stroke-width="1.2"
                stroke-linecap="round"
              />
            </svg>
            <input
              type="password"
              v-model="password"
              placeholder="Senha do juramento"
              autocomplete="current-password"
              aria-label="senha"
            />
          </label>

          <div class="options">
            <label class="remember">
              <input type="checkbox" v-model="remember" />
              <span class="checkbox-custom"></span>
              Lembrar-me, Maculado
            </label>
            <a class="forgot" href="#">Esqueci meu juramento</a>
          </div>

          <button class="btn-login" type="submit" :disabled="loading">
            <span v-if="!loading">Ascender ao Trono (Login)</span>
            <span v-else>Forjando o Anel...</span>
          </button>

          <div>
            <!-- Usar router-link para navegação SPA em vez de href -->
            <router-link class="create" to="/RegisterPage">
              Forjar Nova Alma (Criar Conta)
            </router-link>
          </div>
        </form>
      </div>
    </div>
  </div>
  <Footer />
</template>

<script>
import Navbar from "@/components/navBar.vue";
import Footer from "@/components/footerPage.vue";
import { loginUser, setAuthToken } from "@/services/api.js";

export default {
  name: "LoginPage",
  components: {
    Navbar,
    Footer,
  },
  data() {
    return {
      email: "",
      password: "",
      remember: false,
      loading: false,
      errorMessage: "",
    };
  },
  methods: {
    /**
     * Efetua login do usuário.
     * - Valida que os campos foram preenchidos no formulário (precondição: UI faz binding)
     * - Chama `loginUser(email, password)` do serviço `api.js`
     * - Se retornar tokens, persiste (localStorage) e configura header via `setAuthToken`
     * - Redireciona para `/mainPage` em caso de sucesso
     * - Em caso de erro, normaliza a mensagem para exibir em `errorMessage`
     */
    async login() {
      this.errorMessage = "";
      this.loading = true;
      try {
        const res = await loginUser(this.email, this.password);
        // exemplo de dados retornados: { idToken, refreshToken, expiresIn, localId }
        if (res && res.idToken) {
          // salvar token dependendo do comportamento desejado (aqui localStorage)
          localStorage.setItem("idToken", res.idToken);
          // configurar header Authorization apenas se houver token
          setAuthToken(res.idToken);
        }
        if (res && res.refreshToken) {
          localStorage.setItem("refreshToken", res.refreshToken);
        }

        // Redireciona para a rota original (query param do guard) ou fallback para mainPage
        const redirectTo = this.$route.query.redirect || "/mainPage";
        this.$router.push(redirectTo);
      } catch (err) {
        // Preferir console.error para não bloquear a UI com alert nativo
        console.error("Login falhou:", err);
        // err pode ser um objeto vindo do backend
        this.errorMessage =
          (err && err.error && err.error.message) || err.message || String(err);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
/* Variáveis globais (coloque-as no seu arquivo CSS principal ou no App.vue) */
/*
:root {
  --elden-gold: #B89C62;
  --elden-dark-bg: #1A1A1A;
  --elden-text-shadow: 0 0 5px rgba(255, 223, 150, 0.5);
  --elden-light-gold: #d1b480;
  --elden-medium-gray: #2a2a2a;
  --elden-light-text: #f3e7b3;
}
*/
/* Página inteira */
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

.card {
  width: 360px;
  border-radius: 10px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7),
    0 6px 18px rgba(11, 4, 25, 0.5) inset;
  overflow: hidden;
  background: #181818; /* card com cor sólida solicitada */
  border: 1px solid rgba(212, 175, 55, 0.09);
  padding-top: 8px;
}

.card-top {
  height: 120px;
  /* leve brilho dourado para combinar com o tema */
  background: linear-gradient(
    135deg,
    rgba(212, 175, 55, 0.08) 0%,
    rgba(212, 175, 55, 0.03) 60%
  );
  background-size: cover;
}

.card-body {
  padding: 26px 30px 30px 30px;
  text-align: center;
}

.title {
  margin: 0 0 18px 0;
  font-size: 28px;
  color: #f0c84a; /* título dourado mais vibrante */
  text-shadow: 0 3px 14px rgba(0, 0, 0, 0.8), 0 0 18px rgba(34, 28, 12, 0.25);
  font-weight: 700;
  letter-spacing: 1.6px;
  line-height: 1.05;
  text-transform: none;
  position: relative;
}

.title::after {
  content: "";
  display: block;
  width: 90px;
  height: 4px;
  margin: 12px auto 0 auto;
  border-radius: 2px;
  background: linear-gradient(
    90deg,
    rgba(212, 175, 55, 1),
    rgba(212, 175, 55, 0.6)
  );
  box-shadow: 0 2px 8px rgba(212, 175, 55, 0.12);
}

.form {
  display: flex;
  flex-direction: column;
}

.input-wrap {
  display: flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.02);
  border-radius: 26px;
  padding: 10px 14px;
  margin-bottom: 14px;
  border: 1px solid rgba(255, 255, 255, 0.04);
  transition: box-shadow 180ms ease, border-color 180ms ease,
    transform 120ms ease;
}

.input-wrap:focus-within {
  border-color: rgba(212, 175, 55, 0.9);
  box-shadow: 0 6px 30px rgba(212, 175, 55, 0.06),
    0 0 0 4px rgba(212, 175, 55, 0.03) inset;
  transform: translateY(-1px);
}

.input-wrap .icon {
  width: 18px;
  height: 18px;
  margin-right: 12px;
  opacity: 0.95;
}

.input-wrap input {
  border: none;
  outline: none;
  background: transparent;
  flex: 1;
  font-size: 14px;
  color: #f7edd2; /* texto claro sobre fundo escuro */
  padding: 6px 6px;
}

.options {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 13px;
  color: #7b6a56;
  margin-bottom: 12px;
}

.remember {
  display: flex;
  align-items: center;
  gap: 8px;
}
.remember input {
  display: none;
}
.checkbox-custom {
  width: 14px;
  height: 14px;
  border-radius: 4px;
  background: rgba(212, 175, 55, 0.06);
  display: inline-block;
  position: relative;
  border: 1px solid rgba(212, 175, 55, 0.08);
}
.remember input:checked + .checkbox-custom {
  background: #efb810;
}

.forgot {
  color: #f0c84a;
  text-decoration: none;
  font-weight: 600;
}

.btn-login {
  background: linear-gradient(180deg, #e0c07a 0%, #c9a85a 100%);
  color: #14120f; /* Texto escuro no botão dourado */
  border: 1px solid rgba(88, 67, 36, 0.6);
  padding: 12px 22px;
  font-size: 1.05em;
  font-weight: 700;
  cursor: pointer;
  transition: transform 160ms ease, box-shadow 200ms ease;
  box-shadow: 0 10px 30px rgba(40, 30, 10, 0.25),
    inset 0 -6px 10px rgba(0, 0, 0, 0.12);
  border-radius: 4px;
}

.btn-login:hover {
  transform: translateY(-3px);
  box-shadow: 0 18px 40px rgba(50, 35, 10, 0.32),
    0 0 40px rgba(212, 175, 55, 0.06);
}

.btn-login:active {
  transform: translateY(-1px) scale(0.995);
}

.create {
  margin-top: 12px;
  text-align: center;
  color: #f3e7b3;
  font-size: 13px;
}

input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
input:-webkit-autofill:active {
  -webkit-box-shadow: 0 0 0px 1000px rgba(12, 12, 12, 0.98) inset !important;
  box-shadow: 0 0 0px 1000px rgba(12, 12, 12, 0.98) inset !important;
  -webkit-text-fill-color: #f7edd2 !important;
}

/* pequenas responsividades */
@media (max-width: 420px) {
  .card {
    width: 92%;
  }
}
</style>
