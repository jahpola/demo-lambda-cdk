import json

def handler(event, context):
    print("Foo!")
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': "Hello, lambda"
    }
