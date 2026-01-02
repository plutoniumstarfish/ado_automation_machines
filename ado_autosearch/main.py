import requests
from requests.auth import HTTPBasicAuth

organization = "genex2anchetamax"
project = "ado_automation_machines"

PAT = "71A2OfaynYCTFRixetfS2N4kvFVJ08pnhOORDtouuqVgAEZgWIpaJQQJ99CAACAAAAAAAAAAAAASAZDO241I123"

auth = HTTPBasicAuth("", PAT)
headers = {
    "Content-Type": "application/json"
}


#GET https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=4.1
url_repo = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=4.1"


response = requests.get(url_repo, auth=auth, headers=headers)
response.raise_for_status()

repos = response.json()["value"]


def get_repos(repos):
    result = []

    for repo in repos:
        result.append({
            "name": repo["name"],
            "id": repo["id"]
        })

    return result


repos_info = get_repos(repos)


print(repos_info)
 
