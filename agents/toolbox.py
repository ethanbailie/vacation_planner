import requests
import json
import os


def search(query: str) -> str:
    '''
    Takes in a user query and searches it with Serper

    Returns Serper response as a JSON as a String
    '''
    url = "https://google.serper.dev/search"
    payload = json.dumps({
        "q": query
    })

    headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
