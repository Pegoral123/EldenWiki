<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <a href="/">
        <img :src="logo" alt="Título Elden Wiki" class="logo-img" />
      </a>
    </div>
    <ul class="navbar-links">
      <li><a href="/LoginPage" class="link-cadastro">Conectar-se</a></li>
      <li>
        <a
          href="https://discord.gg/q2zkd7k4my"
          target="_blank"
          rel="noopener"
          class="discord-link"
        >
          <i class="bi bi-discord"></i>
        </a>
      </li>
    </ul>
  </nav>
</template>

<script setup>
import logoImg from "@/assets/TITULO_ELDEN_WIKI.png";
const logo = logoImg;
</script>

<style scoped>
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #181818;
  padding: 0 3rem;
  color: #fff;
  border-bottom: 3px solid rgba(212, 175, 55, 0.15);
  height: 80px;
  box-shadow: 0 2px 16px 0 rgba(0, 0, 0, 0.25);
  position: sticky;
  top: 0;
  z-index: 100;
}

.navbar-brand {
  display: flex;
  align-items: center;
}

.logo-img {
  max-height: 70px;
  width: auto;
  display: block;
  transition: transform 0.2s;
}

.logo-img:hover {
  transform: scale(1.05) rotate(-2deg);
}

.navbar-links {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 2.5rem;
  margin: 0;
  padding: 0;
}

.navbar-links a {
  color: #636157;
  text-decoration: none;
  font-size: 1.25rem;
  font-weight: 500;
  transition: color 0.25s, transform 0.25s;
  letter-spacing: 1px;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
}

.navbar-links .link-cadastro {
  color: #efb810; /* título dourado */
  text-shadow: 2px 2px 8px #000, 0 0 16px #222;
  font-weight: bold;
  font-size: 1.3rem;
}

.navbar-links a:hover,
.navbar-links .link-cadastro:hover {
  color: #fffbe6;
  background: rgba(212, 175, 55, 0.08);
  transform: translateY(-2px) scale(1.07);
}

.discord-link {
  font-size: 1.7rem;
  display: flex;
  align-items: center;
  padding: 0.25rem 0.5rem;
}

.discord-link .bi-discord {
  color: #5865f2;
  transition: color 0.2s, transform 0.2s;
}

.discord-link:hover .bi-discord {
  color: #404eed;
  transform: scale(1.2);
}

/* Responsividade simples */
@media (max-width: 700px) {
  .navbar {
    flex-direction: column;
    height: auto;
    padding: 1rem;
  }
  .navbar-links {
    flex-direction: column;
    gap: 1rem;
    margin-top: 0.5rem;
  }
  .logo-img {
    max-height: 50px;
  }
}
</style>
