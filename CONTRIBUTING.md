### Clone the Repository

For further information, see [Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### Enable Commit Signing

For further information, see [Signing Commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)

Running `git config commit.gpgsign true` 

### Use Conventional Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for your commit messages. Commit messages control versioning of odyssey and are also automatically added to the [Changelog](CHANGELOG.md).

### Use a Virtual Environment

See [venv](https://docs.python.org/3/library/venv.html) for more information.

The integrity of the virtual environment and not polluting the rest of your system with packages is essential. We want our tooling to get us the correct set of packages every time we:

- clone the respository
- checkout a different commit
- add/remove/upgrade a dependency

Create a virtual environment using `python -m venv .venv --upgrade-deps`

Activate the virtual environment based on platform. Some examples:

- Windows with pwsh: `./.venv/Scripts/Activate.ps1`

Install `pip-tools` using `pip install -r src/requirements/pip-tools.txt`

Install remaining dependencies using `pip-sync`

### Recommended Workflow

The repository comes with some configuration for Visual Studio Code. You can use any IDE you'd like, but may find working in VSCode an easier path in this repository.

Similarly, you can use any Operating System environment to contribute, but may find it easier to use the same one(s) as existing contributors.

### Line Endings

Line endings matter more than you think. For some good reading see [Mind the End of Your Line](https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/).

In this repository we stick to LF as much as possible. When adding new files, consider the line endings. When editing existing files, if your changes switch the line endings (which may not be obvious depending on your IDE settings), then in a Pull Request your entire file will be seen as a diff.

We have configured specific settings in `.gitattributes` which should apply to all files in the repository.
