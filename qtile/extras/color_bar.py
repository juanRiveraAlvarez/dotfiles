import json
import os
from PIL import Image
background_image = '/home/juan/Pictures/wallpaper2.png'
def color_bar():
    img = Image.open(background_image)
    colores = {"bg-dark":"#{:02x}{:02x}{:02x}".format(img.getpixel((5,5))[0],img.getpixel((5,5))[1],img.getpixel((5,5))[2]),"bg":"#e1d6a9","red":"#cc241d","green":"#98971a","yellow":"#d79921","blue":"#458588","purple":"#b16286","aqua":"#689d6a","gray":"#928374"}
    return colores

