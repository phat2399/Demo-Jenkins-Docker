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
                echo "Testing..."
            }
        }
        stage('Deploy') {
            steps {
                echo 'Dang trien khai container...'
                sh 'docker stop flask-app-container || true'
                sh 'docker rm flask-app-container || true'
                sh 'docker run -d --name flask-app-container -p 8000:8000 your-docker-id/flask-app:latest'
            }
        }
    }
}