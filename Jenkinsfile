node {
    def imgBUService
    def imgBackPub
    def imgFrontend
    def imgTLManager
    def imgTests

    stage('Clonar Repositorio logs-transparentes') {
        git branch: 'main', credentialsId: 'GitHub-Pass', url: 'https://github.com/larc-logs-transparentes/logs-transparentes.git'
    }
    stage('Gerar Imagem BU Service') {
        dir('backend/bu_service'){
            imgBUService = docker.build("ghcr.io/larc-logs-transparentes/bu-service:jk-${env.BUILD_ID}")
        }
    }
    stage('Gerar Imagem Backend Public') {
        dir('backend/public'){
            imgBackPub = docker.build("ghcr.io/larc-logs-transparentes/back-pub:jk-${env.BUILD_ID}")
        }
    }
    stage('Gerar Imagem Frontend') {
        dir('frontend_new'){
            imgFrontend = docker.build("ghcr.io/larc-logs-transparentes/frontend:jk-${env.BUILD_ID}")
        }
    }
    stage('Gerar Imagem TL Manager') {
        dir('tlmanager'){
            imgTLManager = docker.build("ghcr.io/larc-logs-transparentes/tlmanager:jk-${env.BUILD_ID}")
        }
    }
    stage('Clonar Repositório Config'){
        git branch: 'main', credentialsId: 'GitHub-Pass', url: 'https://github.com/larc-logs-transparentes/config.git'
    }

    stage('Executar testes'){

        sh 'docker container rm -f mongo-logst bu-service back-pub tlmanager'
        sh 'docker network rm -f logst'

        sh 'docker network create logst'

        def mongodb = docker.image('mongo:6.0.14').run('-p 27017:27017 -v ./hom/mongo.init.js:/docker-entrypoint-initdb.d/mongo.init.js -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=1234 --name mongo-logst --hostname mongo-logst --network logst')

        def buservice = imgBUService.run('-p 9090:9090 --network logst --name bu-service -e MONGO_URL="mongodb://buuser:bupassword@mongo-logst/bu_service" -e TL_MANAGER_URL="http://tlmanager:8000" -e TREE_NAME_PREFIX="eleicao_" -e TREE_DEFAULT_COMMITMENT_SIZE=8 --hostname bu-service')

        def backpub = imgBackPub.run('-p 8080:8080 --network logst --name back-pub -v ./hom/backend.public.config.json:/app/src/config.json --hostname back-pub')

        def tlmanager = imgTLManager.run('-p 8000:8000 --network logst --name tlmanager -e URL="mongodb://tluser:tlpassword@mongo-logst:27017/tlmanager" --hostname tlmanager')



        dir('hom/tests'){
            imgTests = docker.build("ghcr.io/larc-logs-transparentes/tests:jk-${env.BUILD_ID}")

            sh 'echo "Aguardando 8s."'
            sh 'sleep 8'

            imgTests.inside('--network logst'){
                sh 'pytest'
            }
        }

        tlmanager.stop()
        backpub.stop()
        buservice.stop()
        mongodb.stop()

    }

    stage('Upload Imagens'){

        docker.withRegistry('https://ghcr.io', 'GitHub-Token'){
            imgBUService.push()
            imgBackPub.push()
            imgFrontend.push()
            imgTLManager.push()
        }
    }
}
