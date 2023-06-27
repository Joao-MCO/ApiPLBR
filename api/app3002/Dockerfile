FROM node:18

# configura a pasta que será usada
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package*.json ./
COPY . .




# baixa as bibliotecas usadas
RUN npm install