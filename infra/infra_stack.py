from aws_cdk import (
    core as cdk,
    aws_events_targets as targets,
    aws_events as events,
    aws_lambda as _lambda,
)

from aws_cdk.aws_lambda_python import PythonFunction

class InfraStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
        # EASIER IF SIMPLE python function...
        # my_function = _lambda.Function(self,
        #     "my-function",
        #     runtime=_lambda.Runtime.PYTHON_3_8,
        #     code=_lambda.Code.asset("src"),
        #     handler="main.handler"
        # )

        my_function = PythonFunction(self,
            "my-function",
            entry="src",
            index="main.py",
            handler="handler",
            runtime=_lambda.Runtime.PYTHON_3_8,
        )

        rule = events.Rule(
            self,
            "Rule",
            schedule=events.Schedule.cron(
                minute="0",
                hour="18",
                month="*",
                week_day="MON-FRI",
                year="*"
            )
        )

        rule.add_target(targets.LambdaFunction(my_function))