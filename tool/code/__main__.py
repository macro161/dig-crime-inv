import click


@click.group()
def cli():
    pass


@click.command()
def config():
    pass


@click.command()
@click.option('--start')
def run(start):
    if start == "init":
        print("CLI started correctly")

    pass


cli.add_command(run)
cli.add_command(config)

cli()
