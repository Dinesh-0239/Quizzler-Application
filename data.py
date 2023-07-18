#-------------------------------------------- Connect to API ----------------------------------------------------------#
import requests

#Selecting question type and no. of question
parameters = {
    "amount": 10,
    "type": "boolean",
}

#connecting to the api
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

#get questions data
data = response.json()
question_data = data["results"]
