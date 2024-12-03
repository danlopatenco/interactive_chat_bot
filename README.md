## Scope

An interactive, Dockerized application with the following key components:

- **LangChain**: For building and managing the application's natural language processing workflow.
- **LangSmith**: For tracking and evaluating user interactions and responses.
- **Streamlit**: For creating an intuitive and interactive user interface.
- **Brave Search API**: To perform internet searches and retrieve relevant information.
- **Docker**: For containerization, ensuring easy deployment and consistent environment setup.

## Setup

1. **Clone the Repository**:
   - Clone the application repository:
     ```bash
     git clone https://github.com/danlopatenco/interactive_chat_bot.git
     cd interactive_chat_bot
     ```
   
2. **Environment Configuration**:
   - Open the `env.example` file.
   - Create a `.env` file in the project root.
   - Copy the keys from `env.example` to `.env`.
   - Fill in the relevant keys (e.g., `BRAVE_API_KEY`) with your own values.
   - Keep other parameters unchanged or modify them only if required for your environment.


3. **Build and Run the Docker Container**:
   - Build the Docker image:
     ```bash
     docker build -t interactive_chat_bot .
     ```
   - Run the container with the `.env` file:
     ```bash
     docker run --env-file .env interactive_chat_bot
     ```

4. **Access the Application**:
   - The application will be available on:
     - **Local URL**: [http://localhost:8080](http://localhost:8080)
     - **Network URL**: (e.g., `http://172.17.0.2:8080`)
     - **External URL** (if configured): (e.g., `http://some-public-ip:8080`)
