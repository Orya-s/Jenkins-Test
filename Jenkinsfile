pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from your version control system (e.g., Git)
                checkout scm
            }
        }

        stage('Run Pytest Tests') {
            steps {
                // Run pytest tests
                sh 'pytest your_test_file.py'
            }
        }
    }
}
