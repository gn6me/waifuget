import click
from app.application import imageLoad

@click.command()
@click.option('--rating', default='safe', help='Set rating for images')
@click.option('--tag', default='cat_girl', help='Set tag to search for')
def cli(tag,rating):
    imageGet = imageLoad(tag,rating)
    imageGet.draw()

@click.command()
def version():
    print("waifuimgcli-0.0.1")
