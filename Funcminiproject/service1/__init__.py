import logging
import random, requests
import os
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    endpoint = os.environ["uri"]
    key = os.environ["pkey"]

    getletters = requests.get('service-mp-2.azurewebsites.net/api/service2?code=W2hl07z/ihKC6YRcApIyObCtw0yL6HzfZQEwLNsnkBdIQgJAv3pGQg==')
    getnumbers = requests.get('service-mp-2.azurewebsites.net/api/service3?code=ap3tUNZHQovrt4OpT/WvKXjJ8zwhytLm8yWWPsQjI69ex6yAtrqsNA==')
    letters = getletters.text
    numbers = getnumbers.text
    ans = []

    for i in range(10):
        ans.append(letters[i])
        ans.append(numbers[i])
    output="".join(answer)

    return str(output)


