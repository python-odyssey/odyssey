### Clone the Repository

For further information, see [Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### Enable Commit Signing

For further information, see [Signing Commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)

Running `git config commit.gpgsign true` 

### Use Conventional Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for your commit messages. Commit messages control versioning of odyssey and are also automatically added to the [Changelog](CHANGELOG.md).

### Use a Virtual Environment

See [venv](https://docs.python.org/3/library/venv.html) for more information.

Create a virtual environment using `python -m venv .venv --upgrade-deps`

Activate the virtual environment based on platform. Some examples:

- Windows with pwsh: `./.venv/Scripts/Activate.ps1`

### Recommended Workflow

The repository comes with some configuration for Visual Studio Code. You can use any IDE you'd like, but may find working in VSCode an easier path in this repository.

Similarly, you can use any Operating System environment to contribute, but may find it easier to use the same one(s) as existing contributors.
