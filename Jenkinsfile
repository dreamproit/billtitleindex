@Library('jenkins-shared-lib') _

eksPipeline{
    project = "billtitleindex-chart"
    awsProjectMap = ["739065237548": "develop,stage,prod,preprod,helm_chart_fix"]
    awsClusterMap = ["739065237548": "eks-cluster-main"]
    deployMap = ["helm_chart_fix": "dev", "stage": "stage", "prod": "prod"]
    artifactName = "billtitleindex"
    promotionMap = ["prod": ["from": "stage"], "preprod": ["from": "stage"]]
    valuesTemplatePath = "src/billtitleindex/billtitleindex-chart/values.yaml"
    helmContext = "src/billtitleindex/"
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
