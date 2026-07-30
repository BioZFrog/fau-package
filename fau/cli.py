import click

from fau.core.ireq import install
from fau.core.copytree import copy
from fau.core.bundle import create_copy_and_clean_bundle
from fau.core.todo import main
from fau.core.makereq import reqFile

@click.group()
def cli():
    pass

@cli.command()
def ireq():
    """Installs the current requirements.txt libraries automatically."""
    install()

@cli.command()
def copytree():
    """Copies the current directory's tree structure directly to your clipboard."""
    copy()

@cli.command()
def bundle():
    """Automatically bundles up every file, zips it, and copies it to the clipboard automatically. Note: Works only on Windows."""
    create_copy_and_clean_bundle()

@cli.command()
def todo():
    """A todo tasks program for your powershell."""
    main()

@cli.command()
def makereq():
    """Reads all of the python files in the current directory, and generates a requirements.txt automatically."""
    reqFile()


if __name__ == "__main__":
    cli()