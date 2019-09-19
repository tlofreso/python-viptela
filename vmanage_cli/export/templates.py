    
import click
import json
from cisco_sdwan import vmanage

@click.command()
@click.argument('type', default='all')
@click.option('--file', '-f', help="output File name", required=True)
# @click.option('--type',
#               help="Device type [vedges, controllers]",
#               type=click.Choice(['vedges', 'controllers']))
@click.pass_context
def templates(ctx, type, file):
    """
    Show device information
    """
    vmanage_session = ctx.obj
    click.echo(f'Exporting templates to {file}')
    vmanage_session.export_templates_to_file(file)