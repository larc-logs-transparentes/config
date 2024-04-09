# Configurações para subir em ambiente de Desenvolvimento (dev)

## Execução do MongoBD

```bash
docker run -d --name dev-mongo-logst --network host mongo:6.0.14
```

## Execução dos containers Docker (só os containers que forem de interesse)

```bash
docker run -d --network host --name dev-back-pub larc-et/back-pub:0.0.3
```

```bash
docker run -d --network host --name dev-bu-service larc-et/bu-service:0.0.3
```

```bash
docker run -d --network host --name dev-frontend larc-et/frontend:0.0.3
```

```bash
docker run -d --network host --name dev-tlmanager larc-et/tlmanager:0.0.3
```


## Execução dos container frontend de modo a poder programa-los Docker (só os containers que forem de interesse)
```bash
docker run -p 3000:3000 --network hom-logst -v ./src:/app/src --name dev-frontend larc-et/frontend:0.0.3
```