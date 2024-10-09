""" demo function """

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()


def handler(event: dict, context: LambdaContext) -> dict:
    """does something"""
    try:
        logger.info("Hello from lambda")
        logger.info(event)

    except Exception as e:
        logger.exception(e)
        raise RuntimeError("Blah") from e

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": "Hello, lambda",
    }
