import click
from app.application import imageLoad

@click.command()
@click.option('-r', '--rating', default='general', help='Set rating for images')
@click.option('-t', '--tag', default='cat_girl', help='Set tag to search for')
def cli(tag,rating):
    try:
        imageGet = imageLoad(tag,rating)
        imageGet.draw()
        print("Press ENTER to keep going or type 'n' to stop")

        # Keep prompting until user quits
        while click.confirm('Show another one?', default=True, show_default=False):
            imageGet = imageLoad(tag,rating)
            imageGet.draw()
            print("Press ENTER to keep going or type 'n' to stop")
    except:
        print("Image could not be displayed >_< Please try again!")
