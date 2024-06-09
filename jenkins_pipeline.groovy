pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Проверка кода из репозитория
                git url: 'https://github.com/dimagarn/PE_2_SEM.git', branch: 'main',
                credentialsId: 'github_credents'
            }
        }

        stage('Install dependencies') {
            steps {
                // Установка зависимостей
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Uvicorn') {
            steps {
                // Запуск Uvicorn
                sh 'uvicorn app.main:app --host 0.0.0.0 --port 8000'
            }
        }
    }
}