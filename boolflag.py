import click


@click.command()
@click.option('--shout', is_flag=True)
def cmd(shout):
    msg = 'Hello, World!'
    if shout:
        msg = msg.upper()
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
