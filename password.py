import click


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Your password')
def cmd(password):
    msg = 'Your password: {password}'.format(password=password)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
