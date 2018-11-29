import click


@click.command()
@click.option('--prefix', default='Hello', help='Prefix of greetings.')
def cmd(prefix):
    msg = '{prefix}, World!'.format(prefix=prefix)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
