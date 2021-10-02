import requests
import json

def repo_amount(user):
    if(type(user) == str):
        repoUrl = "https://api.github.com/users/" + user + "/repos"
        repoInfo = requests.get(repoUrl).json()

        for repo in repoInfo:
            counter = 0
            print("Repo Name: " + repo['name'])
            commitUrl = "https://api.github.com/repos/" + user + "/" + repo['name'] + "/commits?page=1&per_page=100"
            commitInfo = requests.get(commitUrl).json()
            for commit in commitInfo:
                counter += 1
            print("# of Commits: " + str(counter))

    else:
        return "Invalid user data"


#repo_amount('mtorres3')