# mainPage.vue

## Visão geral

Componente wrapper para a página principal do aplicativo. Junta `Navbar`, `LocationsSection` e `Footer` para compor a UI principal.

Responsabilidades:

- Montar a estrutura de página e delegar exibição de conteúdo a `LocationsSection`.
- Aplicar o background visual principal desta rota.

## Estrutura

- `<template>`: composição dos componentes.
- `<script setup>`: importa os componentes necessários.
- `<style scoped>`: define estilo do hero (background, alinhamento central).

## Observações

- A maior parte da lógica fica em `LocationsSection`, mantendo `mainPage` como um wrapper leve.
- Útil para inserir metadados de página (titulo, meta tags) se o projeto adicionar SSR ou gerenciamento de head.

## Melhorias sugeridas

- Se for necessário, adicionar lazy-loading de `LocationsSection` via dynamic import para reduzir bundle inicial.
- Adicionar testes visuais (snapshot) para garantir que a composição não quebre.

---
