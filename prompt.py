import click


@click.command()
@click.option('--name', prompt='Name', default='World', help='The person to greet.')
def cmd(name):
    msg = 'Hello, {name}!'.format(name=name)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
