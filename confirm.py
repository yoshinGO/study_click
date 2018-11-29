import click


@click.command()
def cmd():
    if not click.confirm('Do you want to continue?'):
        raise click.Abort()  # Trueの場合に実行されない

    click.echo('Hello, World!')


def main():
    cmd()


if __name__ == '__main__':
    main()
