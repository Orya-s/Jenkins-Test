pipeline {
    agent any

    stages {
        stage('Run Pytest Tests') {
            steps {
                // Run pytest tests
                sh 'python -m pytest test_file.py'
            }
        }
    }
}
