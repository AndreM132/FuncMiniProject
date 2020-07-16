import logging, random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    listletters = []
    for i in range(10):
        listnumbers.append(random.choice(string.ascii_letters))
    char="".join(listletters)

    return str(char)


