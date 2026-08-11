<template>
  <footer class="site-footer">
    <div class="container">
      <p class="copyright">
        Esta página tem direitos autorais a Jhonathan da Silva Pegoral © 2025
      </p>
    </div>
  </footer>
</template>

<script setup></script>

<style scoped>
/* footer styling (cor dourada consistente) */
.site-footer {
  background: #181818;
  border-top: 3px solid rgba(212, 175, 55, 0.15);
  color: #efb810;
  padding: 1rem 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial;
}

.site-footer .container {
  max-width: 1500px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* (duplicated rules removed) */
@media (max-width: 420px) {
  .site-footer p {
    font-size: 14px;
  }
}
</style>
