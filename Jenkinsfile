pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-demo:v1 .'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh 'docker rm -f flask-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-container flask-demo:v1'
            }
        }

    }

}
