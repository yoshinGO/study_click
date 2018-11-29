import click


@click.group()
@click.option('--debug', is_flag=True)
@click.pass_context  # コンテキストをインジェクトする
def cmd(ctx, debug):
    #  インジェクトしたコンテキストに情報を詰める
    ctx.obj['DEBUG'] = debug


@cmd.command()
@click.pass_context
def subcmd(ctx):
    if ctx.obj['DEBUG']:
        #  サブコマンドではコンテキストから情報を取り出す
        click.echo('DEBUG MODE!')
    click.echo('Hello, World!')


def main():
    # コンテキストから参照するアトリビュートを渡す
    cmd(obj={})


if __name__ == '__main__':
    main()
