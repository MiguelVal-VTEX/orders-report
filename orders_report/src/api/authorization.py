import os
from dotenv import load_dotenv
import json
from .rest_caller import api_call 

load_dotenv()

#This module is in charge of creating an authorization token automatically based on the 
#keys provided by the environment

account = os.getenv('ACCOUNT')
environment = os.getenv('ENVIRONMENT')
app_key = os.getenv('APP_KEY')
app_token = os.getenv('APP_TOKEN')

url = f'https://{account}.{environment}/api/vtexid/apptoken/login'

payload = {
  "appkey": app_key,
  "apptoken": app_token
}

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

def auth_token():
    response = api_call('POST', url, headers, payload)
    return response.json()['token']

if __name__ == '__main__':
    auth_token()