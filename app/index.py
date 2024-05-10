from typing import Any


def handler(event: dict, context: Any) -> dict:
    return {
        'statusCode': 200,
        'headers': {
          "Content-Type": "text/html; charset=utf-8"
        },
        'body': "Hello world!!!!",
    }
