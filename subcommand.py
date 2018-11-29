import click


@click.group()
def cmd():
    pass


@cmd.command()
def english():
    click.echo('Hello, World!')


@cmd.command()
def japanese():
    click.echo('Konnichiwa, Sekai!')


def main():
    cmd()


if __name__ == '__main__':
    main()
