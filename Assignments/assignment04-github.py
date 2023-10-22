from github import Github
from config import githubkey
import requests

github_username = 'KenLin765'
repository_name = 'private'

apikey = githubkey  # Use the imported variable
g = Github(apikey)