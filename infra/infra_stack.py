"""create cdk stacks"""

from aws_cdk import (
    Aws,
    aws_logs,
    Stack,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as _lambda_python,
    aws_apigateway as apigw,
)
from constructs import Construct


class InfraStack(Stack):
    """create infra"""

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        powertools_layer = _lambda.LayerVersion.from_layer_version_arn(
            self,
            id="lambda-powertools",
            layer_version_arn=f"arn:aws:lambda:{Aws.REGION}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:10",
        )

        demofunction = _lambda_python.PythonFunction(
            self,
            "demofunction",
            entry="src",
            index="main.py",
            handler="handler",
            architecture=_lambda.Architecture.ARM_64,
            runtime=_lambda.Runtime.PYTHON_3_13,
            layers=[powertools_layer],
            tracing=_lambda.Tracing.ACTIVE,
            memory_size=128,
            log_retention=aws_logs.RetentionDays.ONE_DAY,
            environment={
                "POWERTOOLS_SERVICE_NAME": "demo-function",
                "POWERTOOLS_LOG_LEVE": "INFO",
            },
        )

        api = apigw.RestApi(
            self,
            "demo-api",
            description="Demo API",
            deploy_options=apigw.StageOptions(
                stage_name="prod",
                tracing_enabled=True,
            ),
        )

        lambda_integration = apigw.LambdaIntegration(demofunction, proxy=True)
        api_resource = api.root.add_resource("demo")
        api_resource.add_method("POST", lambda_integration)
