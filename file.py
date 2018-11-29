import click


@click.command()
@click.argument('file', type=click.File('r'))
def cmd(file):
    with file as f:
        while True:
            line = f.readline()
            if not line:
                break
            click.echo(line, nl=False)


def main():
    cmd()


if __name__ == '__main__':
    main()
