pipeline{
 agent any
 environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    stages {
        stage('Build') {
            steps{
                sh '#!/bin/bash -ilex&&docker build -t xcyhbp/flaskapp:latest .'
            }
        }
        stage('login') {
            steps{
                sh '#!/bin/bash -ilex&&echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push') {
            steps{
                sh '#!/bin/bash -ilex&&docker push xcyhbp/flaskapp:latest'
            }
        }
    }
 post {
     always {
		echo 'end'
     }
 }
}
