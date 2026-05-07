pipeline {
    agent any
    stages {
        stage('安装依赖') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('接口测试') {
            steps {
                sh 'pytest test_cases/test_api_auto.py --alluredir=allure-results'
            }
        }
        stage('UI测试') {
            steps {
                sh 'pytest test_cases/test_ui_po.py --alluredir=allure-results'
            }
        }
    }
}