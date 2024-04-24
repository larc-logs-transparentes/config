# Configurações para subir em ambiente sala limpa

## Criação rede dos containers docker

Se a rede Docker ```logst``` ainda não existir, criar por meio do comando:

```bash
docker network create logst
```

## Execução do MongoBD

Acessar a pasta "raiz" de config.

Criar o container Docker.
Especificar a senha do usuário root no parâmetro **MONGO_INITDB_ROOT_PASSWORD**.
No exemplo a senha é 1234:

```bash
docker run -d -p 27017:27017 -v ./config/hom/mongo.init.js:/docker-entrypoint-initdb.d/mongo.init.js -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=1234 --name mongo-logst --hostname mongo-logst --network logst mongo:6.0.14
```


## Execução dos containers Docker

```bash
docker run -d -p 9090:9090 --network logst --name bu-service -e MONGO_URL="mongodb://buuser:bupassword@mongo-logst/bu_service" -e TL_MANAGER_URL="http://tlmanager:8000" -e TREE_NAME_PREFIX="eleicao_" -e TREE_DEFAULT_COMMITMENT_SIZE=8 --hostname bu-service larc-et/bu-service:0.0.3
```

```bash
docker run -d -p 8080:8080 --network logst --name back-pub -v ./config/hom/backend.public.config.json:/app/src/config.json --hostname back-pub larc-et/back-pub:0.0.3
```

```bash
docker run -d -p 3000:3000 --network logst --name frontend -v ./config/hom/frontend.config.json:/app/src/config.json --hostname frontend larc-et/frontend:0.0.3
```

```bash
docker run -d -p 8000:8000 --network logst --name tlmanager -e URL="mongodb://tluser:tlpassword@mongo-logst:27017/tlmanager" --hostname tlmanager larc-et/tlmanager:0.0.3
```

# Execução de testes

Para a realização de testes, é possível criar uma imagem que contém os procedimentos de testes.

Atualmente, os testes requerem uma instância vazia do Mongo. Deste modo, apontar para um Mongo de testes.

Geração da imagem de testes:

- Acessar a pasta ``config/hom/tests``

```bash
    docker build -t 
```