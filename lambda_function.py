# import json

# def lambda_handler(event, context):
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda! from testing team 123 456789')
#     }

import json

def lambda_handler(event, context):
    response_data = {
        'name': 'John Doe',
        'age': 30,
        'phone': '+1-234-567-8901',
        'email': 'johndoe@example.com'
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response_data)
    }
