import click


@click.command()
def cmd():
    click.echo('Hello, World!')


def main():
    cmd()


if __name__ == '__main__':
    main()
