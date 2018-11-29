import click


@click.command()
def cmd():
    age = click.prompt('Please enter your age', type=int)
    click.echo(age)


def main():
    cmd()


if __name__ == '__main__':
    main()
