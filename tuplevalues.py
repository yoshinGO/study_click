import click


@click.command()
@click.option('--values', type=(str, int))
def cmd(values):
    msg = '{s} {i}'.format(s=values[0], i=values[1])
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
