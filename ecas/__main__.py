import click
from click.decorators import group

from ecas.cli import list_ecas_steps as get_info
from ecas.server import run as run_web_server


@click.group()
def group():
    pass


group.add_command(get_info)
group.add_command(run_web_server)

group()
