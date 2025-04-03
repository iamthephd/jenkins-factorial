pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t factorial-api .'
                sh 'echo "Docker build successful"'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'docker run --rm factorial-api pytest -v'
                sh 'echo "Tests completed successfully"'
            }
        }
        
        stage('Deploy') {
            steps {
                // Stop any existing containers
                sh 'docker stop factorial-api-instance'
                
                // Run the container in detached mode
                sh 'docker rm factorial-api-instance'
                sh 'docker run -d -p 9000:9000 --name factorial-api-instance factorial-api'
                sh 'echo "Application deployed at http://localhost:9000"'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Cleaning up...'
        }
    }
}