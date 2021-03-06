import click


@click.command()
@click.option('--age', type=click.IntRange(0, 100, clamp=True), default=18)
def cmd(age):
    msg = 'Your age: {age}'.format(age=age)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
