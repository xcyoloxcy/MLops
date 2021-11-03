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

    }
 post {
     always {
		echo 'end'
     }
 }
}
