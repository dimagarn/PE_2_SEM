pipeline {
    agent any

    tools {
        dockerTool 'docker'
        'Python 3.9.6': 'Python3'
        'DVC': 'DVC'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/dimagarn/PE_2_SEM.git', credentialsId: 'github_credents'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Get DVC credentials') {
            steps {
                withCredentials([file(credentialsId: 'gdrive_credentials', variable: 'gdrive_credentials')]) {
                  sh "cat ${gdrive_credentials} > gdrive.json"
                  }
                sh 'dvc remote modify myremote --local gdrive_service_account_json_file_path gdrive.json'
            }
        }

        stage('Pull Data From DVC') {
            steps {
                sh 'dvc pull'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("fastapi-app")
                }
            }
        }

        stage('Run Docker Image') {
            steps {
                script {
                    docker.image("fastapi-app").run(["-d", "-p", "8000:8000", "fastapi-app"])
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    docker.image("fastapi-app").stop()
                    docker.image("fastapi-app").remove()
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest'
                }
            }
        }
    }
}
