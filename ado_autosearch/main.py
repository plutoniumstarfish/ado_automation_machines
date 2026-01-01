import requests
from requests.auth import HTTPBasicAuth

organization = "genex2anchetamax"
project = "ado_automation_machines"

PAT = ""

auth = HTTPBasicAuth("", PAT)
headers = {
    "Content-Type": "application/json"
}



#GET https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=4.1
url_repo = "https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=4.1"

