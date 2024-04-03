node {
    def imgBUService
    def imgBackPub
    def imgFrontend
    def imgTLManager

    stage('Clonar Repositorio') {
        git branch: 'main', credentialsId: 'GitHub-Pass', url: 'https://github.com/larc-logs-transparentes/logs-transparentes.git'
    }
    stage('Gerar Imagem BU Service') {
        dir('backend/bu_service'){
            imgBUService = docker.build("larc-logs-transparentes/bu-service:jk-${env.BUILD_ID}")
        }
    }
    stage('Gerar Imagem Backend Public') {
        dir('backend/public'){
            imgBackPub = docker.build("larc-logs-transparentes/back-pub:jk-${env.BUILD_ID}")
        }
    }
    stage('Gerar Imagem Frontend') {
        dir('frontend_new'){
            imgFrontend = docker.build("larc-logs-transparentes/frontend:jk-${env.BUILD_ID}")
        }
    }
    stage('Gerar Imagem TL Manager') {
        dir('tlmanager'){
            imgTLManager = docker.build("larc-logs-transparentes/tlmanager:jk-${env.BUILD_ID}")
        }
    }
    /*stage('Upload Imagem - TL Manager'){
        docker.withRegistry('https://registry.hub.docker.com','GitHub-Pass'){
            imgTLManager.push('jk-${env.BUILD_ID}')
        }
    }*/
}
