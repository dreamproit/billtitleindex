@Library('jenkins-shared-lib') _

eksPipeline{
    project = "billtitleindex-chart"
    awsProjectMap = ["739065237548": "develop,stage,prod,preprod"]
    awsClusterMap = ["739065237548": "eks-cluster-main"]
    deployMap = ["develop": "dev", "stage": "stage", "prod": "prod"]
    artifactName = "billtitleindex"
    promotionMap = ["prod": ["from": "stage"], "preprod": ["from": "stage"]]
    valuesTemplatePath = "src/billtitleindex/billtitleindex-chart/values.yaml"
    listCredentials = [
        "SECRET_KEY",
        "POSTGRES_HOST",
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_DB",
        "POSTGRES_PORT",
        "MESSAGE_BROKER_USER",
        "MESSAGE_BROKER_PASSWORD"
    ]
}
