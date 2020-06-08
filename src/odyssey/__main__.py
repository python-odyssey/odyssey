import logging
import click
import click_log
from pathlib import Path
from git import Repo
from semver import VersionInfo
import semver
from functools import cmp_to_key

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

@click.group()
@click_log.simple_verbosity_option(logger)
def main():
    pass

def validate_directory(ctx, param, value):
    directory = Path(value)
    if not directory.is_dir():
        raise click.BadParameter('directory must exist and be a directory')
    return directory.resolve(strict=True)

@main.command()
@click.option('--directory', default='.', callback=validate_directory, help='Directory to release.')
def release(directory):
    click.echo(f"Preparing to release from directory '{directory}'...")
    repository = Repo(directory)
    click.echo("Detected git repository...")
    head = repository.head
    if head.is_detached:
        raise click.ClickException("Current HEAD is detached.")
    click.echo(f"Detected current branch as '{head.reference.name}'...")
    click.echo(f"Searching for most recent release by semver...")
    tags = []
    for tag in repository.tags:
        if not tag.name.startswith('v'):
            continue
        semver_name = tag.name[1:]
        if not VersionInfo.isvalid(tag.name[1:]):
            continue
        tags.append((tag, semver_name))

    tags = sorted(tags, key=cmp_to_key(lambda item1, item2: semver.compare(item1[1], item2[1])))
    print(tags)


@main.command()
def download():
    print('Download')

if __name__ == '__main__':
    main()
