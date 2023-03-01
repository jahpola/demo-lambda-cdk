from aws_cdk import (
    Stack,
    aws_events_targets as targets,
    aws_events as events,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as _lambda_python
)
from constructs import Construct

class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
        my_function = _lambda_python.PythonFunction(self,
            "my-function",
            entry="src",
            index="main.py",
            handler="handler",
            runtime=_lambda.Runtime.PYTHON_3_9,
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