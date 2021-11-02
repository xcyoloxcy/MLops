pipeline{
 agent any
 environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    
    stages {
        stage('gitclone') {
            steps{
                git 'https://github.com/skywateryang/MLops.git'
             }
        }
        // stage可以添加或减少
        stage('Build') {
            steps{
                sh 'docker build -t skywateryang/flaskapp:latest .'
            }
        }
    }
 post {
     always {
		echo 'end'
     }
 }
}