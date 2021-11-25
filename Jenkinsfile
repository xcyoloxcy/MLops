pipeline{
 agent any
 environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    stages {
        stage('Build') {
            steps{
                sh 'sudo docker build -t skywateryang/flaskapp:latest .'
            }
        }
        stage('login') {
            steps{
                sh 'docker login -u skywateryang -p d09990c5-5f47-4f86-af28-80e806c33f00'
            }
        }
        stage('push') {
            steps{
                sh 'docker push skywateryang/flaskapp:latest'
            }
        }
    }
 post {
     always {
		echo 'end'
     }
 }
}
