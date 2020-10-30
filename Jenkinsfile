pipeline {
  environment {
    imagename = "my-flask-image:latest"
    registryCredential = 'julian-dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/julianNinoo/Devops.git', branch: 'master', credentialsId: 'git'])

      }
    }
    stage('Building image') {
      steps{
        script {
	  sh 'cd /home/juliannino00/Devops/practicaFlaskJenkins'
	  sh 'docker build -t my-flask-image:latest .'
        }
      }
    }
    
    stage('remove container') {
      steps{
        script {
          sh 'docker stop $(docker ps -a -q)'
          sh 'docker rm $(docker ps -a -q)'
         }
       }
    }  

    stage('remove images') {
      steps{
        script {
          sh 'docker rmi $(docker images -q)'
          }
        }
      }

    stage('Deploy images') {
      steps{
        sh 'docker run -d -p 5000:5000 my-flask-image'
      }
    }
  }
}
