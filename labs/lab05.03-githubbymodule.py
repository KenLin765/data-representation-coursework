from github import Github
from config import githubkey

github_username = 'KenLin765'
repository_name = 'private'

apikey = githubkey  # Use the imported variable
g = Github(apikey)


repo = g.get_repo(f"{github_username}/{repository_name}")
clone_url = repo.clone_url

print(f"Clone URL for {repository_name}: {clone_url}")

