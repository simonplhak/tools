#!/usr/bin/env python3

import os
import click
from PIL import Image

@click.group()
def cli():
    pass

@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('--width', default=100, help='Width of the resized image.')
@click.option('--height', default=100, help='Height of the resized image.')
@click.option('--output', default='./', help='Path where the resized image will be stored.')
def resize_image(image_path : str, width: int, height: int, output: str):
    """
    Resize an image maintaining its aspect ratio.
    """
    original_image = Image.open(image_path)
    resized_img = original_image.resize((width, height))
    
    # create folder if doesn't exist
    if not os.path.exists(output):
        os.makedirs(output)

    # Prepare output filename
    filename, file_extension = os.path.splitext(os.path.basename(image_path))
    output_filename = f"{filename}_{width}_{height}{file_extension}"
    output_path = os.path.join(output, output_filename)

    # Save the resized image
    resized_img.save(output_path)
    click.echo(f'Resized image saved at {output_path}')

# Here is an example of an additional command
@cli.command()
def hello():
    """
    Just a command that prints Hello World!
    """
    click.echo('Hello World!')

if __name__ == "__main__":
    cli()
