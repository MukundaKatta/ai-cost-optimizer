# Ai Cost Optimizer

Optimize AI infrastructure costs across cloud providers

## Features

- Analyzers - Cache Analyzer
Analyzers - Model Cost
Api
Collectors - Aws
Collectors - Gcp
Recommenders - Model Switching
Recommenders - Rightsizing
Reporting - Monthly Report

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Key Dependencies:** pydantic,fastapi,uvicorn,anthropic,openai,numpy
- **Containerization:** Docker + Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

### Installation

```bash
git clone https://github.com/MukundaKatta/ai-cost-optimizer.git
cd ai-cost-optimizer
pip install -r requirements.txt
```

### Running

```bash
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up
```

## Project Structure

```
ai-cost-optimizer/
├── src/           # Source code
├── tests/         # Test suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## License

MIT
