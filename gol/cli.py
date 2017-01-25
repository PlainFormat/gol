import click
import os
import yaml

from gol.manager import Manager
from gol.constants import *


@click.group(help='Chronolog command line tool.')
def gol():
    pass


@click.command(help='Init new \'local\' Chronolog file.')
@click.option('-f', '--file', help='New chronolog file name.', type=str, default='chronolog.md')
def init(file: str):
    os.mkdir('.gol')
    open(file, 'w').write('')
    with open(LOCAL_CONFIG_PATH, 'w') as outfile:
        yaml.dump(dict(file=file), outfile, default_flow_style=False, allow_unicode=True)


gol.add_command(init)


@click.command(help='Append today\'s head to the file')
def head():
    suc, config = Manager.try_get_config()
    if suc:
        Manager(config).add_today_head()

gol.add_command(head)


@click.command(help='Append activity for current time')
@click.option('--message', '-m', help='Activity description.', type=str, default='')
def act(message: str):
    suc, config = Manager.try_get_config()
    if suc:
        Manager(config).add_activity(message)

gol.add_command(act)
