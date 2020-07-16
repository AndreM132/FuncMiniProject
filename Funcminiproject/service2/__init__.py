import logging, random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    listnumbers = []
    for i in range(10):
        listnumbers.append(str(random.randint(0.9)))
    num = str("".join(listnumbers))

    return str(num)

