import requests
from requests.auth import HTTPBasicAuth
import argparse

parser = argparse.ArgumentParser(description="Azure DevOps repo branch checker")
parser.add_argument(
    "branch",
    help="Branch name (e.g. release/2026.1)"
)

args = parser.parse_args()

branch_name = args.branch
print(f"Branch passed: {branch_name}")


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

for rp in range(len(repos)):
    repos_id = get_repos(repos)[rp]["id"]

    print(repos_id)


    def branch_exists(repos_id, branch_name):
        url = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories/{repos_id}/refs"
        params = {
            "filter": f"heads/{branch_name}",
            "api-version": "7.1-preview.1"
        }

        r = requests.get(url, auth=auth, headers=headers, params=params)
        r.raise_for_status()

        return len(r.json()["value"]) > 0


    exists = branch_exists(repos_id, branch_name)

    if exists:
        print("Branch exists")
    else:
        print("Branch does NOT exist")
 
 
