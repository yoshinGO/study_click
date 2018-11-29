import click


def validate_age(ctx, param, value):
    age = value

    if age < 1:
        raise click.BadParameter('You are liar!')
    if age > 100:
        raise click.BadParameter('Really?!')


@click.command()
@click.option('--age', callback=validate_age, default=18)
def cmd(age):
    msg = 'Your age: {age}'.format(age=age)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
