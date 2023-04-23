FROM python:3.8-slim-buster

# Instale as dependências do sistema
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    apt-transport-https \
    ca-certificates \
    firefox-esr

# Instale o GeckoDriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux-aarch64.tar.gz && \
    tar -xvf geckodriver-v0.33.0-linux-aarch64.tar.gz && \
    chmod +x geckodriver && \
    mv geckodriver /usr/local/bin

# Instale o Selenium e outras dependências do Python
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copie seus arquivos Python e app FastAPI para o container
COPY script.py /
COPY app.py /

# Defina o ponto de entrada para o container
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7000"]
