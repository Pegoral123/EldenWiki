# Elden Wiki - Backend

Este é o backend do **Elden Wiki**, um projeto full-stack de portfólio que une a paixão por Elden Ring com desenvolvimento web. O projeto é uma wiki comunitária que apresenta lore, bosses e regiões do jogo com uma experiência visual imersiva.

O backend fornece uma API REST construída com FastAPI, autenticação via Firebase e serve dados estruturados do jogo para o frontend Vue.js.

## Objetivos do Projeto

- Servir dados estruturados de lore do jogo para o frontend.
- Fornecer endpoints de autenticação (registro/login/verificação de token) via Firebase Auth.
- Demonstrar habilidades de desenvolvimento full-stack (design de API, autenticação, CORS, arquivos estáticos).
- Futuro: integração com Firestore para gerenciamento dinâmico de conteúdo.

## Tecnologias Utilizadas

| Tecnologia | Função |
|------------|--------|
| Python 3.10+ | Linguagem principal do backend. |
| FastAPI | Framework de alta performance para construção da API REST. |
| Uvicorn | Servidor ASGI para executar o backend. |
| Firebase Admin SDK | Autenticação e integração com Firestore. |
| python-dotenv | Gerenciamento de variáveis de ambiente. |

## Estrutura do Projeto

```
back_end/
├── main.py              # Ponto de entrada da aplicação, CORS, arquivos estáticos
├── firebase_config.py   # Inicialização do Firebase Admin e funções auxiliares
├── requirements.txt     # Dependências Python
├── routes/
│   ├── auth.py          # /auth/register, /auth/login, /auth/verify_token
│   ├── bosses.py        # /boss/, /boss/limgrave_bosses, /boss/caelid_bosses
│   └── locations.py     # /locations/limgrave, /locations/liurnia, /locations/caelid
├── static/              # Imagens dos bosses servidas via /static/
└── config/              # Chave de conta de serviço do Firebase (ignorada pelo git)
```

## Endpoints da API

### Regiões (Locations)
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/locations/limgrave` | Informações da região de Limgrave |
| GET | `/locations/liurnia` | Informações da região de Liurnia |
| GET | `/locations/caelid` | Informações da região de Caelid |

### Bosses
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/boss/` | Todos os bosses (proxy da API externa) |
| GET | `/boss/limgrave_bosses` | Lista de bosses de Limgrave |
| GET | `/boss/caelid_bosses` | Lista de bosses de Caelid |

### Autenticação (Auth)
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/auth/register` | Registrar novo usuário (Firebase) |
| POST | `/auth/login` | Login com email e senha |
| POST | `/auth/verify_token` | Verificar token ID do Firebase |

## Como Executar o Backend

### Pré-requisitos

- Python 3.10+ instalado
- pip instalado
- Projeto Firebase com chave de conta de serviço

### Passos

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Pegoral123/EldenWiki.git
   cd EldenWiki/back_end
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure as credenciais do Firebase:**
   - Coloque seu arquivo `ServiceAccountKey.json` em `back_end/config/`
   - Crie um arquivo `.env` com `FIREBASE_API_KEY=sua_chave_web_api_do_firebase`

6. **Inicie o servidor backend:**
   ```bash
   uvicorn main:app --reload
   ```

7. **Acesse a API:**
   - API: http://localhost:8000
   - Documentação Swagger: http://localhost:8000/docs

## Variáveis de Ambiente

Crie um arquivo `.env` na pasta `back_end/`:

```
FIREBASE_API_KEY=sua_chave_web_api_do_firebase
```

## Melhorias Futuras (Roadmap)

- Migrar dados de bosses/regiões de dicionários hardcoded para o Firestore
- Painel admin para gerenciamento de conteúdo (CRUD de bosses/regiões)
- Sistema de comentários de usuários nas regiões e bosses
- Rate limiting nos endpoints de autenticação
- Deploy na nuvem (Render, Railway ou Google Cloud Run)