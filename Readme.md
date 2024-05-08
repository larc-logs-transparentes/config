# Configuração

## Sobre 

Esse Readme contém informações para a criação e execução de containers Docker.

Os passos para a geração das imagens é o mesmo para qualquer configuração de ambiente:
- ```dev``` aka desenvolvimento;
-  ```hom``` aka homologação ou sala-limpa; ou
-  ```prod``` aka ambiente de produção.

Já os passos para a execução de containers são deferentes dependendo do ambiente.
Para esse caso, há arquivos separados para cada ambiente.


## Geração das imagens Docker


Sob a pasta ``backend/public``:
```bash
docker build -t larc-et/back-pub:0.0.3 .
```
Sob a pasta ``backend/bu_service``:
```bash
docker build -t larc-et/bu-service:0.0.3 .
```
Sob a pasta ``frontend_new``:
```bash
docker build -t larc-et/frontend:0.0.3 .
```
Sob a pasta ``tlmanager``:
```bash
docker build -t larc-et/tlmanager:0.0.3 .
```

Docker de testes (projeto config):
So a pasta ``config/hom/tests``
```bash
docker build -t larc-et/tests:0.0.3 .
```


## Execução dos containers Docker

Para o ambiente de homologação (ou sala-limpa), veja o arquivo [```hom/Readme.md```](./hom/Readme.md).

Para o ambiente de desenvolvimento (ou dev), veja o arquivo [```dev/Readme.md```](./dev/Readme.md).

Para o ambiente de produção (ou prod), veja o arquivo [```prod/Readme.md```](./prod/Readme.md).