pipeline {
    agent any
    stages {
        stage('checkout code') {
            steps {
                git url:'https://github.com/Qurram-Farooqui/streamlitapp.git', branch:'main'
            }
        }
        stage('Cleanup Stage') {
            steps{
                sh 'docker rm -f $(docker ps -aq)'
            }
        }
        stage('Build Docker image') {
            steps {
                sh 'docker build -t myapp .'
            }

        }
        stage('Create Container') {
            steps{
                sh 'docker run -d -p 8501:8501 myapp'
        }
    }
}
}