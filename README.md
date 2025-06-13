# AI-Powered Test Case Generation Service

This project is a robust backend service that leverages Google's Gemini AI (gemini-2.0-flash API) to automatically generate high-quality test cases and their documentation for code. Built with a modern microservices architecture, it combines **FastAPI** for a high-performance web framework, **Celery** for asynchronous task processing, and **Docker** for containerized deployment. This provides developers with a scalable, reliable solution to streamline testing workflows.

## Key Features

- **Automated Test Generation**:  
  Users provide source code, programming language (e.g., Python, JavaScript), and testing framework (e.g., Pytest, Jest). The system generates relevant test code and detailed test case documentation.
  
- **Asynchronous Task Processing**:  
  Utilizes a Celery task queue to handle time-consuming AI generation requests in the background, ensuring responsive API endpoints and preventing timeouts.

- **Scalable Architecture**:  
  Modular design allows independent scaling of components (web service, Celery workers, message broker) to meet growing traffic demands.

- **Containerized Deployment**:  
  Includes Dockerfile and docker-compose configurations for easy building, deployment, and consistent environments across development and production.

- **Secure Configuration Management**:  
  Sensitive data (e.g., API keys) are loaded via environment variables, and unnecessary files are excluded using `.gitignore` for secure version control.

## Technology Stack

- **Web Framework**: FastAPI
- **AI Model**: Google Gemini API (gemini-2.0-flash)
- **Asynchronous Task Queue**: Celery (with Redis/RabbitMQ as message broker)
- **Programming Language**: Python 3.8+
- **Containerization**: Docker, Docker Compose
- **Dependency Management**: Pydantic

## Use Cases

This project is ideal for:

- **Developers**: Quickly generate tests for new features or existing code to boost efficiency.
- **QA Engineers**: Automate test script and documentation creation to reduce manual effort.
- **CI/CD Pipelines**: Integrate into automated pipelines for continuous testing.
- **Learning & Exploration**: Explore integrating large language models into real-world web services.

With this service, we aim to simplify test development, allowing developers to focus on core logic while ensuring software quality.

## Setup Instructions

**Note**: You need to create a `.env` file in the project root directory to store sensitive configuration, such as the Gemini API key. The `.env` file should include the following content:

```plaintext
GEMINI_API_KEY="your_GEMINI_API_KEY"
