import requests
import os

token = os.environ['AZURE_TOKEN']

url = 'https://graph.microsoft.com/v1.0/users'
headers = {
  'Authorization': token
}

graph_result = requests.get(url=url, headers=headers)

print(graph_result.json())