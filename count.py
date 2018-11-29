import click


@click.command()
@click.option('-v', '--verbose', count=True)
def cmd(verbose):
    msg = 'Verbosity: {v}'.format(v=verbose)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
