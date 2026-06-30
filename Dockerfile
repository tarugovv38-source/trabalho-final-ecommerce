# Imagem base oficial do Python 3.11 em versão enxuta (slim)
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências primeiro (aproveita o cache do Docker)
COPY api/requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da API
COPY api/ .

# Expõe a porta 5000 que a API utiliza
EXPOSE 5000

# Comando para iniciar a API quando o container subir
CMD ["python", "app.py"]
