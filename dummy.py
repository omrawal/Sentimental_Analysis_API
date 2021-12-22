import requests
import json
URL = "http://localhost:5000/"
PARAM = ['I am so sad', "All the misfortunes are given to me", "This was a very bad day"
         "I was in an accident and now I have to pay for my car's reapirs. I am already short on money and I am not sure if I will even be able to pay rent next week"]

r = requests.get(url=URL+str(PARAM))
data = r.json()

print(data['sentence_list'])
print(data['score'])
