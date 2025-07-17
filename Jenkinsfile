pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Dang build Docker image...'
                // Thay 'your-docker-id/flask-app' bang ten ban muon
                sh 'docker build -t your-docker-id/flask-app:latest .'
            }
        }
        stage('Test') {
            steps {
                echo "Dang chay kiem thu tu dong..."
                script {
                    // Chay pytest ben trong Docker image vua build de dam bao
                    // moi truong test giong het moi truong se deploy.
                    // Container se tu dong bi xoa sau khi chay xong test.
                    sh 'docker run --rm your-docker-id/flask-app:latest pytest'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Dang trien khai container....'
                sh 'docker stop flask-app-container || true'
                sh 'docker rm flask-app-container || true'
                sh 'docker run -d --name flask-app-container -p 8000:8000 your-docker-id/flask-app:latest'
            }
        }
    }
}
