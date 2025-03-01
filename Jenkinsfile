pipeline {
    agent any
    stages {
        stage('Clone repo') {
            steps {
                git 'https://github.com/IDBVietNam/cnx.git'
            }
        }
        stage('Setup Environment') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cnx:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 8000:8000 cnx:latest'
            }
        }
    }
}
