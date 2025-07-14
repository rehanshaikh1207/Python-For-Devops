# Devops Engineer - developer has api(application programable interface)
# https://jsonplaceholder.typicode.com/posts

import requests

def get_api_data():
    url_demo = "https://catfact.ninja/fact"

    response = requests.get(url=url_demo)
    return response.json()

print(get_api_data())

