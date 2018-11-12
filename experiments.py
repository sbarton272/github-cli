"""Learning the API"""
import os

from github import Github

TOKEN = os.environ['GITHUB_TOKEN']
CLIENT = Github(TOKEN)

PR_OPEN = 'open'

REPO = 'BranchIntl/BranchServer'
AUTHOR = 'sbarton272'

def get_my_prs(client, repo_name, author):
    repo = client.get_repo(repo_name)
    pulls = repo.get_pulls(state=PR_OPEN)
    authored = [pull for pull in pulls if pull.user.login == author]

    # TODO pr.base.label

if __name__ == '__main__':
    print(get_my_prs(CLIENT, REPO, AUTHOR))
