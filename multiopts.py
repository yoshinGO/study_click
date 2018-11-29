import click


@click.command()
@click.option('--values', multiple=True)
def cmd(values):
    for value in values:
        click.echo(value)


def main():
    cmd()


if __name__ == '__main__':
    main()
