# Configurações para rodar o sistema em um ambiente de produção

## Premissas

Algumas premissas antes dos procedimentos:

1) A pré-existência de um database Mongo DB, com pares de usuários e senhas para as collections: **bu_service** e **tlmanager**.
Para subir uma instância do MongoDB inicial, pode ser utilizado o procedimento extra [Criação de MongoDB](#criação-de-mongodb) Em Configurações Opcionais.

2) A pré-existência de um par de chave pública e privada (no formato PKCS8) acessíveis no filesystem para uso do microserviço **TLManager**


## Configuração

Ume vez que a configuração permaneça a mesma:
- Geometria e endereço do MongoDB;
- Par de chaves do TL Manager

Não será necessário realizar a configuração uma vez que ela esteja ok.

Passos de configuração:

1) Acessar a pasta ``config/prod``

2) Editar o arquivo ``backend.public.config.json`` e alterar o atributo ``mongodb_config.hostname`` (ver abaixo) de modo a apontar para o endereço do MongoDB, com usuário e senha de acesso para o DB ``bu_service``:

    ```bash
    ...
        "mongodb_config": {
            "hostname": "mongodb://USUARIO_BU:SENHA_BU@ENDERECO_MONGO",
            "port": 27017,
            "database": "bu_service"
        },
    ...
    ```

3) Editar o arquivo ``.env`` e editar as duas linhas que contém as variáveis de ambiente com as URLs que apontam para o MongoDB (com usuário e senha):

    ```bash
    TL_MANAGER_MONGO_URL=mongodb://tluser:tlpassword@endereco-mongodb:27017/tlmanager
    BU_SERVICE_MONGO_URL=mongodb://buuser:bupassword@endereco-mongodb:27017/bu_service
    ```

4) Editar o arquivo ``.env`` e editar as duas linhas que contém os endereços completos dos arquivos com as chaves (pública e privada) para o TL Manager:

    ```bash
    TL_MANAGER_PUB_KEY_PATH=/path/completo/para/chavepublica.pem
    TL_MANAGER_PRIV_KEY_PATH=/path/completo/para/chaveprivada.pem
    ```


## Execução

Certificar-se de que:
- não existam containers em execução e; 
- as portas **8000**, **3000**, **8080** e **9000** estejam disponíveis para uso na máquina.


### Comando para executar os containers (docker compose)

1) Acessar a pasta ``config/prod``

2) Executar:

    ```bash
    docker compose up
    ```


### Comando para finalizar os containers

1) Acessar a pasta ``config/prod``

2) Executar:

    ```bash
    docker compose down
    ```

# Configurações Opcionais

## Criação de MongoDB

Caso se deseje iniciar uma instância do MongoDB separadamente, ela pode ser iniciada com os procedimentos a seguir:

1) Acessar a pasta ``config/prod``

2) Executar:

    ```bash
    docker run -d -p 27017:27017 \
        --name mongo-logst --hostname mongo-logst \
        -v ./../hom/mongo.init.js:/docker-entrypoint-initdb.d/mongo.init.js \
        -e MONGO_INITDB_ROOT_USERNAME=root \
        -e MONGO_INITDB_ROOT_PASSWORD=1234 \
        mongo:6.0.14
    ```
