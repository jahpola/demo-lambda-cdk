""" demo function """

from aws_lambda_powertools import Logger,Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()
tracer = Tracer()
app = APIGatewayRestResolver()

@app.post("/hello")
@tracer.capture_method
def hello() -> dict:
    """returns hello"""
    return {"message": "Hello, world!"}

@tracer.capture_lambda_handler
def handler(event: dict, context: LambdaContext) -> dict:
    """lambda handler"""
    logger.info("Start")
    return app.resolve(event, context)
