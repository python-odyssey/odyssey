import click

@click.group()
def main():
    print('Hello, World!')

@main.command()
def release():
    print('Release')

@main.command()
def download():
    print('Download')

if __name__ == '__main__':
    main()
