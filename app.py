#!/usr/bin/env python3
from aws_cdk import core as cdk
from infra.infra_stack import InfraStack

app = cdk.App()
InfraStack(app, "DemoLambdaStack")

app.synth()
