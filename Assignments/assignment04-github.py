from github import Github
from config import githubkey

# Details of username, repo, file path on github and text to replace
github_username = 'KenLin765'
repository_name = 'data-representation-coursework'
file_path = 'Assignments/replace.txt'
replacement_text = 'Kenneth'

apikey = githubkey  # Use the imported variable
g = Github(apikey)

# Get repository
repo = g.get_user(github_username).get_repo(repository_name)

# Used as basis to figure out how to download file - https://github.com/PyGithub/PyGithub/issues/1343
# Get content of files
file = repo.get_contents(file_path)

original_content = file.decoded_content.decode("utf-8")

# https://www.w3schools.com/python/ref_string_replace.asp 
# - I used replace method and I set the replacement text earlier in the script
# Replaces 'Andrew' with 'Kenneth'
modified_content = original_content.replace('Andrew', replacement_text)

# Commit the changes to repo
repo.update_file(
    # Sets file path from variable
    path=file_path,
    message=f"This has replaced Andrew with '{replacement_text}' in file located in '{file_path}",
    # Pushes Modified Content variable with amended text
    content=modified_content,
    # This was giving me error, I was unaware of it prior
    # Secure Hash Algorithm is a check used to make changes to latest version
    sha=file.sha
)
