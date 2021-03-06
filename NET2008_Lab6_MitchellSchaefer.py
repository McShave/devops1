from github import Github
import yaml

# credentials.yml contains your usr/repo and PAT created in step 11 above
# So we load the data into a YML object
data = yaml.safe_load(open('credentials.yml'))

# Extract the user and token from the data object
# 0. Complete these 2 lines below
user = data['creds']['username']
token = data['creds']['token']

# using an access token
g = Github(token)
repo = g.get_repo(user)

## Complete your tasks from here
# 1. Get all branches you have created for your public repo

print("branches = ", list(repo.get_branches()))

# 2. Get all pull requests you have created

print("pulls = ", list(repo.get_pulls()))

# 3. Get a list of commits you have created in your `main` branch.

commits = repo.get_commits(sha='main')
print("commits from branch = ", list(commits))