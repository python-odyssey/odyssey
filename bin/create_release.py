import os
import subprocess
import git
import logging
import toml
import semver
from semantic_release.history import get_current_version_by_tag, get_new_version
from semantic_release.history.logs import evaluate_version_bump
import github

PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PYPROJECT_TOML_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pyproject.toml'))

def assert_clean_master():
    repository = git.Repo(PROJECT_ROOT_PATH)
    active_branch = repository.active_branch
    assert active_branch.name == 'master', f'Repository on branch {active_branch.name} is not currently on the master branch!'
    #assert not repository.is_dirty(index=True, working_tree=True, untracked_files=True), 'Repository contents are dirty!'

def get_current_project_version() -> str:
    with open(PYPROJECT_TOML_PATH, 'r') as file_stream:
        pyproject_toml = toml.load(file_stream)
    return pyproject_toml

def set_current_project_version(pyproject_toml):
    with open(PYPROJECT_TOML_PATH, 'w') as file_stream:
        toml.dump(pyproject_toml, file_stream)

def assert_current_project_version_semver(current_project_version):
    assert semver.VersionInfo.isvalid(current_project_version), f"{current_project_version} is not a valid semver version!"

def enable_semantic_release_logging():
    logger = logging.getLogger("semantic_release")
    logger.setLevel(logging.DEBUG)

def assert_releaseable_changes_detected(current_tagged_version):
    bump_string = evaluate_version_bump(current_tagged_version)
    assert bump_string, 'semantic-release would not create a release!'
    return bump_string

assert_clean_master()
pyproject_toml = get_current_project_version()
current_project_version = pyproject_toml['tool']['poetry']['version']
assert_current_project_version_semver(current_project_version)
enable_semantic_release_logging()
current_tagged_version = get_current_version_by_tag()
bump_string = 'minor'#assert_releaseable_changes_detected(current_tagged_version)
new_version = get_new_version(current_tagged_version, bump_string)
print(f"Creating {bump_string} release! Bumping from version {current_tagged_version} to version {new_version}!")
pyproject_toml['tool']['poetry']['version'] = new_version
set_current_project_version(pyproject_toml)