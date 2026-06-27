# API E-Commerce — Trabalho Final Cloud Computing

**Instituição:** UNIDAVI — Centro Universitário para o Desenvolvimento do Alto Vale do Itajaí  
**Curso:** Bacharelado em Sistemas de Informação  
**Disciplina:** Cloud Computing  
**Professor:** Prof. Esp. Ademar Perfoll Junior  
**Aluno:** (seu nome aqui)  
**Tema:** Infraestrutura para um Pequeno E-Commerce  

---

## Descrição

API REST desenvolvida em Python com Flask, simulando o backend de um pequeno e-commerce.  
A API expõe endpoints para consulta de produtos, com pipeline de Integração Contínua configurado via GitHub Actions.

---

## Estrutura de Diretórios

```
trabalho-final-ecommerce/
├── api/
│   ├── app.py               # Código principal da API
│   ├── requirements.txt     # Dependências do projeto
│   ├── data/
│   │   └── produtos.json    # Dados simulados (10 produtos)
│   └── tests/
│       └── test_api.py      # Testes unitários (pytest)
├── .github/
│   └── workflows/
│       └── ci.yml           # Pipeline de CI com GitHub Actions
└── README.md
```

---

## Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git

---

## Execução Local (sem container)

### 1. Clone o repositório

```bash
git clone https://github.com/tarugovv38-source/trabalho-final-ecommerce.git
cd trabalho-final-ecommerce
```

### 2. Instale as dependências

```bash
pip install -r api/requirements.txt
```

### 3. Execute a API

```bash
cd api
python app.py
```

A API estará disponível em: `http://localhost:5000`

---

## Endpoints Disponíveis

| Método | Rota                        | Descrição                         |
|--------|-----------------------------|-----------------------------------|
| GET    | `/status`                   | Health check da aplicação         |
| GET    | `/produtos`                 | Lista todos os produtos           |
| GET    | `/produtos?categoria=Redes` | Filtra produtos por categoria     |
| GET    | `/produtos/{id}`            | Retorna um produto pelo ID        |

### Exemplos de uso

```bash
curl http://localhost:5000/status
curl http://localhost:5000/produtos
curl http://localhost:5000/produtos/1
curl http://localhost:5000/produtos/9999   # Retorna 404
```

---

## Execução dos Testes

```bash
cd api
pytest tests/ -v
```

Para executar com relatório de cobertura:

```bash
cd api
pytest tests/ -v --cov=app --cov-report=term
```

---

## Integração Contínua

O pipeline de CI é executado automaticamente a cada `push` na branch `main` via GitHub Actions.

**Etapas do pipeline:**
1. Checkout do código
2. Configuração do Python 3.11
3. Instalação das dependências
4. Análise estática de código com `flake8`
5. Execução dos testes com cobertura via `pytest-cov`

---

## Execução com Docker (opcional)

> Caso queira testar em container futuramente:

```bash
# Construir imagem
docker build -t api-ecommerce .

# Executar container
docker run -p 5000:5000 api-ecommerce
```
