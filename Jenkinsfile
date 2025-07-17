pipeline {
    agent any
    environment {
        // QUAN TRỌNG: Tất cả các giá trị phải được đặt trong dấu ngoặc kép ""
        AWS_ACCOUNT_ID      = "927875589544"
        AWS_DEFAULT_REGION  = "ap-southeast-1"
        ECR_REPOSITORY_NAME = "demolab8"
        EKS_CLUSTER_NAME    = "demo-eks"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${ECR_REPOSITORY_NAME}:latest ."
            }
        }
        stage('Push to Amazon ECR') {
            steps {
                // Sử dụng withCredentials để nạp AWS credentials một cách an toàn
                // 'aws-credentials-lab' là ID bạn đã đặt ở Bước 1.5
                withCredentials([aws(credentials: 'aws-credentials-lab')]) {
                    script {
                        def ecrUri = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${ECR_REPOSITORY_NAME}:latest"
                        sh "docker tag ${ECR_REPOSITORY_NAME}:latest ${ecrUri}"
                        // Lệnh aws bây giờ sẽ tự động sử dụng credentials đã được nạp
                        sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                        sh "docker push ${ecrUri}"
                    }
                }
            }
        }
        stage('Deploy to EKS') {
            steps {
                // Tương tự, nạp credentials cho các lệnh kubectl
                withCredentials([aws(credentials: 'aws-credentials-lab')]) {
                    script {
                        sh "aws eks --region ${AWS_DEFAULT_REGION} update-kubeconfig --name ${EKS_CLUSTER_NAME}"
                        sh "kubectl apply -f deployment.yaml"
                        sh "kubectl apply -f service.yaml"
                    }
                }
            }
        }
    }
}