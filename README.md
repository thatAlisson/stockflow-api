<!-- LANG SWITCHER -->
<p align="center">
  <a href="#pt-br">🇧🇷 Português</a> • 
  <a href="#en-us">🇺🇸 English</a>
</p>

---

<a name="pt-br"></a>
# 📦 StockFlow API (Português)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

API RESTful desenvolvida para gerenciamento de estoque e controle logístico de armazéns. O sistema controla entradas e saídas de mercadorias, previne a venda sem saldo disponível e valida níveis mínimos para evitar a ruptura de estoque.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI** (Alta performance e documentação Swagger automática)
- **SQLAlchemy** (ORM para mapeamento relacional)
- **Pydantic** (Validação de schemas e contratos de dados)
- **SQLite / PostgreSQL** (Persistência de dados)
- **Docker & Docker Compose** (Containerização de ambiente)

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados.

### Passo a Passo

1. Clone o repositório:
   ```bash
   git clone [https://github.com/thatAlisson/stockflow-api.git](https://github.com/thatAlisson/stockflow-api.git)
   cd stockflow-api
