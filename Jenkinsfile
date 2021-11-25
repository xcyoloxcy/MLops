pipeline{
 agent any
	
    stages {
        stage('Build') {
            steps{
                sh 'sudo docker build -t skywateryang/flaskapp:latest .'
            }
        }

    }
 post {
     always {
		echo 'end'
     }
 }
}
