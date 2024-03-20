# Configurações para subir em ambiente de Desenvolvimento (dev)

## Execução do MongoBD

```bash
docker run -d --name dev-mongo-tse --network host mongo:6.0.14
```

## Execução dos containers Docker (só os containers que forem de interesse)

```bash
docker run -d --network host --name dev-tse-back-priv larc-et/tse-back-priv:0.0.1
```

```bash
docker run -d --network host --name dev-tse-back-pub larc-et/tse-back-pub:0.0.1
```

```bash
docker run -d --network host --name dev-tse-frontend larc-et/tse-frontend:0.0.1
```

```bash
docker run -d --network host --name dev-tlmanager larc-et/tlmanager:0.0.1
```