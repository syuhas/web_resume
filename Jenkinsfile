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
        stage('Register Task Definition') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: "aws credentials",
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    script {
                        def taskDefinition = """
                        {
                            "family": "jenkinsDocker",
                            "requiresCompatibilities": ["FARGATE"],
                            "networkMode": "awsvpc",
                            "cpu": "256",
                            "memory": "512",
                            "arn:aws:iam::551796573889:role/ecsTaskExecutionRole",
                            "containerDefinitions": [
                                {
                                    "name": "jrepo",
                                    "image": "551796573889.dkr.ecr.us-east-1.amazonaws.com/jrepo:latest",
                                    "essential": true,
                                    "memory": 512,
                                    "cpu": 256,
                                    "portMappings": [
                                        {
                                            "containerPort": 80,
                                            "hostPort": 80
                                        }
                                    ]
                                }
                            ]
                        }
                        """
                        writeFile file: 'task-definition.json', text: taskDefinition
                        sh 'aws ecs register-task-definition --cli-input-json file://task-definition.json'
                    }
                }
            }
        }
        stage('Update ECS Service') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: "aws credentials",
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    script {
                        def taskDefinitionArn = sh(
                            script: "aws ecs describe-task-definition --task-definition jenkinsDocker --query 'taskDefinition.taskDefinitionArn' --output text",
                            returnStdout: true
                        ).trim()
                        sh "aws ecs update-service --cluster jenkinsDocker --service webResume --task-definition ${taskDefinitionArn}"
                    }
                }
            }
        }
    }
}