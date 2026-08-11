<template>
  <!-- Navbar global do site -->
  <Navbar />
  <div
    class="hero"
    :style="{ backgroundImage: `url(${require('@/assets/fundo_4.webp')})` }"
  >
    <div class="card">
      <div class="card-body">
        <h2 class="title">Forjar Nova Alma</h2>
        <!-- Formulário de registro de usuário
             - on submit chama método `register`
             - mostra mensagens de erro/sucesso acima dos campos
        -->
        <form @submit.prevent="register" class="form">
          <div v-if="errorMessage" class="form-error">{{ errorMessage }}</div>
          <div v-if="successMessage" class="form-success">
            {{ successMessage }}
          </div>

          <label class="input-wrap">
            <svg class="icon" viewBox="0 0 24 24" fill="none">
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
              type="text"
              v-model="name"
              placeholder="Nome do Maculado"
              autocomplete="name"
              aria-label="nome"
            />
          </label>

          <label class="input-wrap">
            <svg class="icon" viewBox="0 0 24 24" fill="none">
              <path
                d="M12 12c2.761 0 5-2.239 5-5s-2.239-5-5-5-5 2.239-5 5 2.239 5 5 5z"
                stroke="#fff"
                stroke-width="1.2"
              />
            </svg>
            <input
              type="email"
              v-model="email"
              placeholder="Email (ex: voce@exemplo.com)"
              autocomplete="email"
              aria-label="email"
            />
          </label>

          <label class="input-wrap">
            <svg class="icon" viewBox="0 0 24 24" fill="none">
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
              placeholder="Senha (mín. 8 caracteres)"
              autocomplete="new-password"
              aria-label="senha"
            />
          </label>

          <label class="input-wrap">
            <svg class="icon" viewBox="0 0 24 24" fill="none">
              <rect
                x="3"
                y="11"
                width="18"
                height="10"
                rx="2"
                stroke="#fff"
                stroke-width="1.2"
              />
            </svg>
            <input
              type="password"
              v-model="confirmPassword"
              placeholder="Confirmar senha"
              autocomplete="new-password"
              aria-label="confirmar-senha"
            />
          </label>

          <button class="btn-login" type="submit" :disabled="loading">
            <span v-if="!loading">Forjar Alma (Registrar)</span>
            <span v-else>Forjando...</span>
          </button>

          <router-link to="/login" class="create"
            >Já tenho alma (Login)</router-link
          >
        </form>
      </div>
    </div>
  </div>
  <Footer />
</template>

<script>
import Navbar from "@/components/navBar.vue";
import Footer from "@/components/footerPage.vue";
import { registerUser, setAuthToken } from "@/services/api.js";

export default {
  name: "RegisterPage",
  components: { Navbar, Footer },
  data() {
    return {
      // campos do formulário
      name: "",
      email: "",
      password: "",
      confirmPassword: "",
      // estado de submissão
      loading: false,
      // mensagens exibidas na UI
      errorMessage: "",
      successMessage: "",
    };
  },
  methods: {
    /**
     * register
     * Handler do submit do formulário de registro.
     * - Valida campos localmente (nome, email, senha e confirmação)
     * - Chama `registerUser` do serviço `api.js`
     * - Em caso de sucesso, armazena token(s) e redireciona para `/mainPage`
     * - Em caso de erro, normaliza a resposta e exibe mensagem amigável
     *
     * Entradas via data(): name, email, password, confirmPassword
     * Efeitos colaterais: altera `loading`, `errorMessage`, `successMessage`, sessionStorage e rota
     */
    async register() {
      // reset das mensagens de UI
      this.errorMessage = "";
      this.successMessage = "";

      // normalização/trim de entradas
      const name = (this.name || "").trim();
      const email = (this.email || "").trim();
      const password = this.password || "";
      const confirm = this.confirmPassword || "";

      // validações básicas no cliente (evitar chamadas desnecessárias ao backend)
      if (!name) {
        this.errorMessage = "Informe seu nome, Maculado.";
        return;
      }
      if (!email) {
        this.errorMessage = "Informe um email válido.";
        return;
      }
      const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRe.test(email)) {
        this.errorMessage = "Email inválido.";
        return;
      }
      if (password.length < 8) {
        this.errorMessage = "A senha precisa ter ao menos 8 caracteres.";
        return;
      }
      if (password !== confirm) {
        this.errorMessage = "As senhas não conferem.";
        return;
      }

      // indica que a submissão está em progresso
      this.loading = true;
      try {
        const res = await registerUser(name, email, password);
        // Se o backend devolver tokens, podemos autenticar imediatamente
        if (res && res.idToken) {
          // guarda token no serviço e no sessionStorage para persistência temporária
          setAuthToken(res.idToken);
          sessionStorage.setItem("idToken", res.idToken);
          if (res.refreshToken)
            sessionStorage.setItem("refreshToken", res.refreshToken);
          // redireciona para a página principal após registro
          this.$router.push({ path: "/mainPage" });
          return;
        }

        // se o backend não retornar token, exibir mensagem genérica de sucesso
        this.successMessage = "Conta criada com sucesso.";
      } catch (err) {
        // normalização de erros esperados do axios / backend
        console.error("Erro no registro:", err);
        const resp =
          err && err.response && err.response.data ? err.response.data : err;
        if (resp) {
          if (Array.isArray(resp.detail)) {
            this.errorMessage = resp.detail
              .map((d) => d.msg || d.message || JSON.stringify(d))
              .join("; ");
          } else if (resp.detail) {
            this.errorMessage = resp.detail;
          } else if (resp.message) {
            this.errorMessage = resp.message;
          } else if (typeof resp === "string") {
            this.errorMessage = resp;
          } else {
            this.errorMessage = "Erro ao criar conta.";
          }
        } else {
          this.errorMessage = "Erro desconhecido.";
        }
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
/* Reaproveita estilos semelhantes ao LoginPage para manter tema */
.hero {
  /* idem ao login */
  position: relative;
  width: 100%;
  min-height: 100vh;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  text-align: center;
  font-family: serif;
}
.card {
  width: 420px;
  border-radius: 10px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7);
  overflow: hidden;
  background: #181818;
  border: 1px solid rgba(212, 175, 55, 0.09);
  padding-top: 8px;
}
.card-body {
  padding: 26px 30px 30px 30px;
  text-align: center;
}
.title {
  margin: 0 0 18px 0;
  font-size: 28px;
  color: #f0c84a;
  text-shadow: 0 3px 14px rgba(0, 0, 0, 0.8);
  font-weight: 700;
  letter-spacing: 1.6px;
}
.title::after {
  content: "";
  display: block;
  width: 90px;
  height: 4px;
  margin: 12px auto 0;
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
  color: #f7edd2;
  padding: 6px 6px;
}
.options {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  font-size: 13px;
  color: #7b6a56;
  margin-bottom: 12px;
}

.btn-login {
  background: linear-gradient(180deg, #e0c07a 0%, #c9a85a 100%);
  color: #14120f;
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
.btn-login:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.form-error {
  background: rgba(180, 20, 20, 0.12);
  color: #ffcccc;
  border: 1px solid rgba(180, 20, 20, 0.22);
  padding: 10px;
  border-radius: 6px;
  margin-bottom: 12px;
}
.form-success {
  background: rgba(40, 120, 40, 0.08);
  color: #dff5d9;
  border: 1px solid rgba(40, 120, 40, 0.12);
  padding: 10px;
  border-radius: 6px;
  margin-bottom: 12px;
}
.create {
  margin-top: 14px;
  color: #f3e7b3;
}
@media (max-width: 520px) {
  .card {
    width: 95%;
    margin: 0 10px;
  }
  .title {
    font-size: 22px;
  }
}
</style>
