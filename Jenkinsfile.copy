pipeline {
    agent any

    stages {
        stage('BuildandPublishECR') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: "aws credentials",
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 551796573889.dkr.ecr.us-east-1.amazonaws.com'
                    sh 'docker build -t jrepo .'
                    sh 'docker tag jrepo:latest 551796573889.dkr.ecr.us-east-1.amazonaws.com/jrepo:latest'
                    sh 'docker push 551796573889.dkr.ecr.us-east-1.amazonaws.com/jrepo:latest'
                    
                }
            }
        }
        stage('TestRepo') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: "aws credentials",
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh "aws ecr list-images --repository-name jrepo --region us-east-1"
                }
                
            }
        }
        stage('PublishECS') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: "aws credentials",
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh 'aws ecs update-service --cluster jenkinsDocker --service webResume --force-new-deployment --region us-east-1'
                }
                
            }
        }
    
        stage('CleanupServer') {
            steps {
                echo "docker system prune -f -a"
                
            }
        }
    
    }   
}       