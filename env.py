import click


@click.command()
@click.option('--shell', envvar='SHELL')
def cmd(shell):
    click.echo(shell)


def main():
    cmd()


if __name__ == '__main__':
    main()
