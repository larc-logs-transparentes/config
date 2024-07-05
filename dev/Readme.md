# Configurações para subir em ambiente de Desenvolvimento (dev)

## Geração das imagens Docker

Acessar a pasta ``logs-transparentes/backend/bu_service`` e executar:

```bash
docker build -t larc-et/bu-service:local .
```

Acessar a pasta ``logs-transparentes/backend/public`` e executar:

```bash
docker build -t larc-et/back-pub:local .
```

Acessar a pasta ``logs-transparentes/frontend_new`` e executar:

```bash
docker build -t larc-et/frontend:local .
```

Acessar a pasta ``logs-transparentes/tlmanager`` e executar:

```bash
docker build -t larc-et/tlmanager:local .
```

Alternativamente, todas imagens podem ser geradas com o script ``gerar-imagens.sh``, executando o comando:

```bash
./gerar-imagens.sh
```

## Execução do ambiente

O ambiente de desenvolvimento pode ser executado de uma única vez com auxílio do ``docker compose``.

Mas caso se deseje subir individualmente cada instância, podem ser executados os comandos das próximas seções.

#### Execução do MongoBD

```bash
docker run -d --name dev-mongo-logst --network host mongo:6.0.14
```

#### Execução dos containers Docker (só os containers que forem de interesse)

```bash
docker run -d --network host --name dev-back-pub larc-et/back-pub:local
```

```bash
docker run -d --network host --name dev-bu-service larc-et/bu-service:local
```

```bash
docker run -d --network host --name dev-frontend larc-et/frontend:local
```

```bash
docker run -d --network host --name dev-tlmanager larc-et/tlmanager:local
```


## Execução dos container frontend de modo a poder programa-los Docker (só os containers que forem de interesse)
```bash
docker run -p 3000:3000 --network hom-logst -v ./src:/app/src --name dev-frontend larc-et/frontend:0.0.3
```