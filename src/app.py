import json

def lambda_handler(event, context):
    # Extract 'event' query param from event['queryStringParameters']
    query = event.get("queryStringParameters", {})
    event_value = query.get("event", "not provided")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello from SAM Lambda!",
            "event_param": event_value,
            "raw_input": event
        })
    }
