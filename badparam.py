import click


@click.command()
@click.option('--age', type=int, help='Your age.')
def cmd(age):
    if age < 1:
        raise click.BadParameter('You are liar!')
    if age > 100:
        raise click.BadParameter('Really?!')

    msg = 'Your age: {age}'.format(age=age)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
