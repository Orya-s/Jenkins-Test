pipeline {
    agent any

    stages {
        stage('Run Tests and Sleep') {
            parallel {
                stage('Run Pytest Tests') {
                    steps {
                        // Run pytest tests
                        sh 'pip install pytest'
                        sh 'python3 -m pytest test_file.py'
                    }
                }

                stage('Sleep') {
                    steps {
                        // sleep
                        sleep(time: 3, unit: 'SECONDS')
                    }
                }
            }
        }
    }
}
