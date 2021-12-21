import json
import requests

request_parameters = {
    "amount" : 10,
    "type" : "boolean",
}

response = requests.get(url="https://opentdb.com/api.php",params = request_parameters)
response.raise_for_status()
question_data = response.json()["results"]