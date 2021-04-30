def setBuildName(){
    currentBuild.displayName = "${BUILD_NUMBER}_${envName}_${selectedTest}"
}

pipeline {

    environment{

    }
    agent{
        label 'master'
    }
    stages{

        stage('Run Jenkins docker-slave'){
            agent{
                docker {
                    image "jenkins-slave"
                    label "master"
                }
            }
            stages{
                stage('Run tests'){
                    steps{
                        lock(env.email){
                            script{

                                def test_case = "./tests"


                                try{
                                    def robotCmd = "robot"
                                    robotCmd = robotCmd + " " + "${test_case}"
                                    sh "${robotCmd}"
                                }
                                catch(Exception e){
                                    echo "Environment:" + e
                                    currentBuild.result = "UNSTABLE"
                                }
                            }
                        }
                    }
                }
                stage('Publish Robot Framework results'){
                    steps{
                        step([
                            $class : 'RobotPublisher',
                            outputPath : '.',
                            outputFileName : "output.xml",
                            reportFileName : "report.html",
                            logFileName : "log.html",
                            disableArchiveOutput : false,
                            enableCache: true,
                            passThreshold : 100,
                            unstableThreshold: 80.0,
                            otherFiles : "*.png",
                        ])
                    }
                }
            }
        }
    }
}