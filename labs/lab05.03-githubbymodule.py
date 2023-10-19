from github import Github
from config import githubkey

apikey = githubkey  # Use the imported variable
g = Github(apikey)
for repo in g.get_user().get_repos():
    print(repo.name)