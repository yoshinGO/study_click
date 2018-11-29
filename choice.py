import click


@click.command()
@click.option('--language', type=click.Choice(['Japanese', 'English']))
def cmd(language):
    click.echo(language)


def main():
    cmd()


if __name__ == '__main__':
    main()
