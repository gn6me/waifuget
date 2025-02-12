import click
from app.application import imageLoad

@click.command()
@click.option('-r', '--rating', default='general', help='Set rating for images')
@click.option('-t', '--tag', default='cat_girl', help='Set tag to search for')
def cli(tag,rating):
    imageGet = imageLoad(tag,rating)
    imageGet.draw()
    while click.confirm('Show another one?', default=True):
        imageGet = imageLoad(tag,rating)
        imageGet.draw()
