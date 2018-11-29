import click


@click.command()
@click.option('--upper', 'transformation', flag_value='upper')
@click.option('--lower', 'transformation', flag_value='lower', default=True)
def cmd(transformation):
    click.echo(transformation)


def main():
    cmd()


if __name__ == '__main__':
    main()
