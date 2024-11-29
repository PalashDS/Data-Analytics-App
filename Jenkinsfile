pipeline { 
    agent any 

    stages { 

        stage('Build') { 
            steps { 
                sh 'pip install -r requirements.txt' 
            } 
        } 

        stage('Test') { 
            steps { 
                sh 'pytest' 
            } 
        } 

        stage('Docker Build') { 
            steps { 
                script { 
                    docker.build('my-python-app:latest') 
                } 
            } 
        } 

        stage('Deploy to Minikube') { 
            steps { 
                script { 
                    // Set the Docker environment to Minikube and build the Docker image
                    sh '''
                        eval $(minikube docker-env) 
                        docker build -t my-python-app:latest .
                    '''
                    // Apply the Kubernetes deployment configuration
                    sh 'kubectl apply -f k8s-deployment.yaml' 
                } 
            } 
        } 

    } 
}
