import click


@click.command()
@click.argument('path', type=click.Path(exists=True))
def cmd(path):
    click.echo(path)
    filename = click.format_filename(path, shorten=True)
    click.echo(filename)


def main():
    cmd()


if __name__ == '__main__':
    main()
