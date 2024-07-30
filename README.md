# Crowdbotics Codespace Starter

This repository contains the starter template for a GitHub Codespace that is preconfigured for this research project.

## Contents

This codespace template includes the following:

- A Python 3.12 environment installed from the default Microsoft Devcontainer registry.
- A Docker configuration for local and web codespaces development, including a PostgreSQL database.
  - PostgreSQL runs on its default port 5432.
- Zsh shell

### Preinstalled Python Packages

- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic
- Pyscopg2
- Python Dotenv
- Python Multipart

#### Preinstalled Python Packages for Development

- Black
- Pytest
- Pytest-cov
- Coverage

### Preinstalled VS Code Extensions

- Python
- Pylance
- Black formatter
- SQL Tools for PostgreSQL

## Getting Started

### Github Codespaces on the Web

Open the repository on Github as a Codespace.

### Local Development

1. Install the VSCode Devcontainer extension.
2. Open the repository in VSCode.

## Running the Application

### Using DevContainers

This project is set up to be used with Visual Studio Code DevContainers. To start the application:

1. Open the project in Visual Studio Code.
2. Reopen the project in a DevContainer.
3. The application will automatically build and start.

### Using Docker Compose

Alternatively, you can run the application using Docker Compose:

```sh
docker-compose up --build
```
