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
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u DOCKERHUB_CREDENTIALS_USR --password-stdin'
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
