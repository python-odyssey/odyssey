import argparse
from github import Github

parser = argparse.ArgumentParser()
parser.add_argument('--token', required=True)
parser.add_argument('--tag', required=True)
parser.add_argument('--message', required=True)
parsed_args = parser.parse_args()

github = Github(login_or_token=parsed_args.token)
repository = github.get_repo('python-odyssey/odyssey')
tags = repository.get_tags()
found_tag = None
for tag in tags:
    if parsed_args.tag == tag.name:
        found_tag = tag.name

assert found_tag, f"{parsed_args.tag} not found in repository."

response = repository.create_git_release(tag=found_tag, name=found_tag, message=parsed_args.message)
print(response)
