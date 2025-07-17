pipeline {
    agent any
    environment {
        AWS_ACCOUNT_ID      = "927875589544" 
        AWS_DEFAULT_REGION  = "ap-southeast-1"    
        ECR_REPOSITORY_NAME = "demolab8" // Tên repo ECR 
        EKS_CLUSTER_NAME    = "demo-eks" // Tên cluster EKS 
    }
    stages {
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${ECR_REPOSITORY_NAME}:latest ."
            }
        }
        stage('Push to Amazon ECR') {
            steps {
                script {
                    def ecrUri = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${ECR_REPOSITORY_NAME}:latest"
                    sh "docker tag ${ECR_REPOSITORY_NAME}:latest ${ecrUri}"
                    sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                    sh "docker push ${ecrUri}"
                }
            }
        }
        stage('Deploy to EKS') {
            steps {
                script {
                    sh "aws eks --region ${AWS_DEFAULT_REGION} update-kubeconfig --name ${EKS_CLUSTER_NAME}"
                    sh "kubectl apply -f deployment.yaml"
                    sh "kubectl apply -f service.yaml"
                }
            }
        }
    }
}