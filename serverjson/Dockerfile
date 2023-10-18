# Use a imagem oficial do Node.js como etapa intermediária
FROM node:18 AS node_stage

WORKDIR /usr/src/app

# Instale as dependências Node
COPY package*.json ./
RUN npm install

# Use a imagem base Python para a etapa final
FROM python:3.10-slim

WORKDIR /usr/src/app

# Instale Node.js
RUN apt-get update && apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Copie o node_modules da etapa intermediária
COPY --from=node_stage /usr/src/app/node_modules ./node_modules
COPY package*.json ./

# Instale as dependências Python
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copie o resto dos arquivos do projeto para o container
COPY . .

# Exponha a porta 6060 para o Express
EXPOSE 6060

# Comando para iniciar o servidor Express
CMD [ "node", "serverjson.js" ]
