node {
    def imgTseBackPriv
    def imgTseBackPub
    def imgTseFrontend
    def imgTLManager

    stage('Clonar Repositorio') {
        git branch: 'main', credentialsId: 'GitHub-Pass', url: 'https://github.com/larc-logs-transparentes/logs-transparentes.git'
    }
    stage('Gerar Imagem TSE backend private') {
        dir('backend/private'){
            imgTseBackPriv = docker.build("larc/logst-tse-back-priv:jk-${env.BUILD_ID}")
        }
    }
    stage('Gerar Imagem TSE backend public') {
        dir('backend/public'){
            imgTseBackPub = docker.build("larc/logst-tse-back-pub:jk-${env.BUILD_ID}")
        }
    }
    stage('Gerar Imagem TSE frontend') {
        dir('frontend_new'){
            imgTseFrontend = docker.build("larc/logst-tse-frontend:jk-${env.BUILD_ID}")
        }
    }
    stage('Gerar Imagem TL Manager') {
        dir('tlmanager'){
            imgTLManager = docker.build("larc/logst-tlmanager:jk-${env.BUILD_ID}")
        }
    }
    stage('Upload Imagem - TL Manager'){
        docker.withRegistry('https://registry.hub.docker.com','DockerHub-Pass'){
            imgTLManager.push('jk-${env.BUILD_ID}')
        }
    }
}
