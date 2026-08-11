# LoginPage.vue

## Visão geral

Componente de autenticação (Login) que permite ao usuário acessar a aplicação.
Nome do componente: `LoginPage`.

Principais responsabilidades:

- Receber email e senha do usuário.
- Chamar `loginUser(email, password)` em `src/services/api.js`.
- Persistir tokens retornados (`idToken`, `refreshToken`) e configurar Authorization header via `setAuthToken`.
- Redirecionar para `/mainPage` em caso de sucesso.
- Exibir mensagens de erro amigáveis.

## Estrutura

- `<template>`: contém o formulário com campos de email/senha, opção "Lembrar-me" e link para cadastro.
- `<script>`: contém a lógica de submissão (método `login`) e estado reativo (`email`, `password`, `remember`, `loading`, `errorMessage`).
- `<style scoped>`: estilos visuais responsivos e consistentes com tema do site.

## Detalhes importantes

- O template agora usa `<router-link to="/register">` para navegação interna (SPA).
- `login()` trata erros sem usar `alert()` — mensagens são normalizadas para `errorMessage` e exibidas na UI.
- `setAuthToken` é chamado somente quando o backend retorna `idToken`.

## Melhorias sugeridas

- Implementar política de "lembrar sessão" usando `remember` (por exemplo escolher entre sessionStorage/localStorage).
- Adicionar validação client-side antes da submissão (ex.: checar formato de email e campo vazio).
- Criar testes unitários para o fluxo de login e tratamento de erros.

## Como testar

1. Rodar frontend:

```powershell
npm install
npm run serve
```

2. Acessar rota de login e testar:

- login com credenciais válidas (verificar redirecionamento e tokens no localStorage)
- login inválido (verificar `errorMessage` visível)

---

Se quiser, posso adicionar testes unitários (Vue Test Utils) cobrindo os cenários mais comuns.
