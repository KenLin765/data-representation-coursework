from github import Github
from config import githubkey
import requests

github_username = 'KenLin765'
repository_name = 'private'

apikey = githubkey  # Use the imported variable
g = Github(apikey)


repo = g.get_repo(f"{github_username}/{repository_name}")
clone_url = repo.clone_url

print(f"Clone URL for {repository_name}: {clone_url}")

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + " more stuff \n"

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print (gitHubResponse)


