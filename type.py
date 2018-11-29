import click


@click.command()
@click.option('--age', type=int, help='Your age.')
def cmd(age):
    msg = 'Your age: {age}'.format(age=age)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
