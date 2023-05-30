#**************************************************************************************
#
# data.py
# Remarks: This makes a call to an API to get random questions from openTDB website
#
#***********************************************************************************

import requests # Allows to make a request via the API

#Create a dictionary that will hold the parameters of the data from the request
parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)# Make the API request
response.raise_for_status() #Make sure API reauest was successful (i.e. code 200 and not codes 400, etc.)
data = response.json() #Place all data retrieved via the API into a json format
question_data = data["results"] # Passes all data to the dictonary which will be accessed via the main.py file.

