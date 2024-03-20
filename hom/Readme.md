# Configurações para subir em ambiente sala limpa

## Criação rede dos containers docker

Se a rede Docker ```tse``` ainda não existir, criar por meio do comando:

```bash
docker network create tse
```

## Execução do MongoBD

Acessar a pasta "raiz" de config.

Criar o container Docker.
Especificar a senha do usuário root no parâmetro **MONGO_INITDB_ROOT_PASSWORD**.
No exemplo a senha é 1234:

```bash
docker run -d -p 27017:27017 -v ./config/hom/mongo.init.js:/docker-entrypoint-initdb.d/mongo.init.js -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=1234 --name mongo-tse --hostname mongo-tse --network tse mongo:6.0.14
```


## Execução dos containers Docker

```bash
docker run -d -p 9090:9090 --network tse --name tse-back-priv -v ./config/hom/backend.private.config.json:/app/src/config.json --hostname tse-back-priv larc-et/tse-back-priv:0.0.1
```

```bash
docker run -d -p 8080:8080 --network tse --name tse-back-pub -v ./config/hom/backend.public.config.json:/app/src/config.json --hostname tse-back-pub larc-et/tse-back-pub:0.0.1
```

```bash
docker run -d -p 3000:3000 --network tse --name tse-frontend -v ./config/hom/frontend.config.json:/app/src/config.json --hostname tse-frontend larc-et/tse-frontend:0.0.1
```

```bash
docker run -d -p 8000:8000 --network tse --name tlmanager -e URL="mongodb://logsuser:logspassword@mongo-tse:27017/logsT" --hostname tlmanager larc-et/tlmanager:0.0.1
```