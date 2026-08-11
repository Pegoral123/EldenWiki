# Elden Wiki - Front-End

A personal, full-stack development project aimed at honing my programming skills and serving as a key piece of my professional portfolio.

Elden Wiki seeks to be a community-driven repository for information, trivia, and fan theories about the Elden Ring universe. It also provides a space for the community to share ideas, ask questions, and discuss their latest discoveries.

## Project Goals

The main purpose of the Elden Wiki is to create an informative and collaborative environment around the Elden Ring lore, allowing:

- Users to explore curiosities and data about the game.
- The community to submit questions and comments.
- Me to demonstrate and practice full-stack development skills, from database modeling to front-end responsiveness.

## Technologies Used

This project uses a modern, decoupled architecture, separating the client (Frontend) and the data service (Backend).

### Frontend

| Technology | Role |
|------------|------|
| Vue.js     | Primary framework for the user interface and component-based structure. |
| Axios      | API consumption and request management. |
| Node.js    | Runtime environment for execution and dependency management. |

### Backend

| Technology | Role |
|------------|------|
| Python     | The core programming language. |
| FastAPI    | High-performance, modern framework for building a REST API. |
| Uvicorn    | ASGI server used to run the backend application. |

## Future Implementations (Roadmap)

- System for comments and user registration.
- Integration with MySQL for relational database modeling.
- Secure authentication with Two-Factor Verification via email.
- Cloud deployment (e.g., AWS, Azure, or Google Cloud) to make the project publicly accessible.

## How to Run the Project (Frontend)

This guide is for setting up the frontend. Please ensure you have the backend server running separately to fetch data via the API.

### Prerequisites

Make sure you have Node.js and npm installed on your machine.

### Steps

1. Clone this repository:
   ```bash
    git clone https://github.com/Pegoral123/Elden_Wiki_Front.git

2. **Navigate to the project directory:**
   ```bash
    cd Elden_Wiki_Front

4. **Install the dependencies:**
   ```bash
    npm install
   
5. **Start the development server:**
    ```bash
    npm run serve
   
