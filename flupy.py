import typer
import os
from colorama import Fore, Style

from pathlib import Path


app = typer.Typer()


projects_dirs = []


def generate_flutter_projects_directories(directory):
    global projects_dirs

    projects_dirs = []

    cwd = os.getcwd()
    pwd = Path(cwd).joinpath(directory)
    dirs = list(filter(lambda d: d.is_dir(), pwd.iterdir()))

    for d in dirs:
        if "pubspec.yaml" in os.listdir(d):
            projects_dirs.append(d)


def run_command(command: str, directory: str):
    cwd = os.getcwd()
    pwd = Path(cwd).joinpath(directory)
    for d in projects_dirs:
        os.chdir(pwd.joinpath(d))
        print(f"{Fore.GREEN}>> {d} <<{Style.RESET_ALL}")

        os.system(command)

        os.chdir(pwd)


@app.command()
def clean(directory):
    generate_flutter_projects_directories(directory)
    run_command("flutter clean", directory)


@app.command()
def get(directory):
    generate_flutter_projects_directories(directory)
    run_command("flutter pub get", directory)


if __name__ == "__main__":
    app()
