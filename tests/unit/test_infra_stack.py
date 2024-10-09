""" define tests """

from cdk_nag import AwsSolutionsChecks
from aws_cdk import (
    assertions,
    Aspects,
    App,
)

from infra.infra_stack import InfraStack
import pytest

@pytest.fixture(scope="module",name="template")
def setup_template():
    """define a basic app """
    app = App()
    stack = InfraStack(app, "teststack")
    template = assertions.Template.from_stack(stack)
    yield template

def test_lambda_function_created(template):
    """test that lambda function is created"""
    template.has_resource_properties(
        "AWS::Lambda::Function", {"Handler": "main.handler", "Architectures": ["arm64"]}
    )


def test_solutions_checks():
    """test that solutions checks are in place"""
    app = App()
    Aspects.of(app).add(AwsSolutionsChecks())
