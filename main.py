from fetch_data import Fetch
from web_server import Server
from table import Table
import click

fetch = Fetch()
data = fetch.get_device_list()


@click.group()
def cli():
    pass

@click.command()
def serve():
    server = Server(data)
    server.start_server()

@click.command()
def showtable():
    table = Table()
    create_table = table.create_table(data)
    print(create_table)

cli.add_command(serve)
cli.add_command(showtable)

if __name__ == "__main__":
    cli()
