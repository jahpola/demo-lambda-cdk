""" define tests """

import aws_cdk as core

from cdk_nag import AwsSolutionsChecks

from aws_cdk import (
    assertions,
    Aspects,
)
from infra.infra_stack import InfraStack


def test_lambda_function_created():
    """test that lambda function is created"""
    app = core.App()
    stack = InfraStack(app, "teststack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::Lambda::Function", {"Handler": "main.handler", "Architectures": ["arm64"]}
    )


def test_solutions_checks():
    """test that solutions checks are in place"""
    app = core.App()
    Aspects.of(app).add(AwsSolutionsChecks())
