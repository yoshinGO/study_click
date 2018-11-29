import random

import click


@click.command()
@click.option('--age', default=lambda: random.randint(1, 100))
def cmd(age):
    msg = 'Your age: {age}'.format(age=age)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
