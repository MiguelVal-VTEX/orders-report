import requests
import json
from python_graphql_client import GraphqlClient
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT = os.getenv('ACCOUNT')
ENVIRONMENT = os.getenv('ENVIRONMENT')


def api_call(
    method: str, 
    url: str,
    headers: str, 
    payload: str
    ) -> requests.Response: 

    """A function to execute rest API calls

    Keyword arguments:
    method  -- the http verb used for the operation
    url     -- the endpoint in which the request will be sent
    headers -- parameters send with channel information, specifically acceptance protocols and authentication
    payload -- data within the API call
    
    Returns:
        response: request.Response -- API call response formated as a requests object
    """    
    
    data = json.dumps(payload)
    response = requests.request(method, url, headers=headers, data = data)

    return response

def graphql_call(
    action: str, 
    variables: str, 
    headers: str
    ) -> requests.Response:
    
    '''Executes a graphQL based API
    
    action      -- Defines wether the call will be a mutation or a query. It contains the definition for the call aswell
    variables   -- Variables set for the call
    headers     -- Authentication data
    
    Returns:
        response: request.Response -- API call response formated as a requests object
    
    '''
    
    client = GraphqlClient(f'https://{ACCOUNT}.{ENVIRONMENT}/_v/private/graphql/v1')
    response = client.execute(action,variables=variables, headers=headers)

    print(json.dumps(response, indent=2))

    return response
