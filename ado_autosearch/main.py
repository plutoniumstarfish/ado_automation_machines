import requests
from requests.auth import HTTPBasicAuth

organization = "genex2anchetamax"
project = "ado_automation_machines"

PAT = "rgnVYQZRFwp92wPX0NmozclOy8w3EZWWxGLv3utcw2eeVa3qD1Q4JQQJ99CAACAAAAAAAAAAAAASAZDO1AwR1strgnVYQZRFwp92wPX0NmozclOy8w3EZWWxGLv3utcw2eeVa3qD1Q4JQQJ99CAACAAAAAAAAAAAAASAZDO1AwR1strgnVYQZRFwp92wPX0NmozclOy8w3EZWWxGLv3utcw2eeVa3qD1Q4JQQJ99CAACAAAAAAAAAAAAASAZDO1AwR1strgnVYQZRFwp92wPX0NmozclOy8w3EZWWxGLv3utcw2eeVa3qD1Q4JQQJ99CAACAAAAAAAAAAAAASAZDO1AwR1strgnVYQZRFwp92wPX0NmozclOy8w3EZWWxGLv3utcw2eeVa3qD1Q4JQQJ99CAACAAAAAAAAAAAAASAZDO1AwR1st"

auth = HTTPBasicAuth("", PAT)
headers = {
    "Content-Type": "application/json"
}



#GET https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=4.1
url_repo = "https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=4.1"

response = requests.get(url_repo, auth=auth, headers=headers)
response.raise_for_status()

repos = response.json()["value"]

for repo in repos:
    print(repo["name"], repo["id"])response = requests.get(url, auth=auth, headers=headers)
response.raise_for_status()

repos = response.json()["value"]

for repo in repos:
    print(repo["name"], repo["id"])response = requests.get(url, auth=auth, headers=headers)
response.raise_for_status()

repos = response.json()["value"]

for repo in repos:
    print(repo["name"], repo["id"])

