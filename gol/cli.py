import click

from gol.manager import Manager


@click.group(help='Chronolog command line tool.')
def gol():
    pass


@click.command(help='Append today\'s head to the file')
@click.argument('filename', nargs=1)
def head(filename: str):
    Manager(filename).add_today_head()

gol.add_command(head)


@click.command(help='Append activity for current time')
@click.argument('filename', nargs=1)
@click.option('--message', '-m', help='Activity description.', type=str, default='')
def act(filename: str, message: str):
    Manager(filename).add_activity(message)

gol.add_command(act)
