pipeline{
 agent any
	
    stages {
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
