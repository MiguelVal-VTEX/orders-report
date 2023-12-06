import requests
import json
from python_graphql_client import GraphqlClient
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT = os.getenv('ACCOUNT')
ENVIRONMENT = os.getenv('ENVIRONMENT')


def api_call(method, url,headers, payload):

    #Calls requests based on API Rest
    data = json.dumps(payload)
    response = requests.request(method, url, headers=headers, data = data)

    #print(response.json()['token'])

    return response

def graphql_call(action, variables, headers):
    #Calls requests based on GraphQL Client
    client = GraphqlClient(f'https://{ACCOUNT}.{ENVIRONMENT}/_v/private/graphql/v1')
    response = client.execute(action,variables=variables, headers=headers)

    print(json.dumps(response, indent=2))

    return response
