import json
import os
from PIL import Image
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir,'..','data','autostart.json')
with open(json_file_path,'r') as  f:
    data = json.load(f)
background_image= data["autostart"][0][14:-2]
print(background_image)
json_file_path = os.path.join(current_dir,'..','data','gruvbox.json')
with open(json_file_path,'r') as  f:
    data = json.load(f)
def color_bar():
    img = Image.open(background_image)
    colores = data['colores']
    colores['bg-dark']="#{:02x}{:02x}{:02x}".format(img.getpixel((5,5))[0],img.getpixel((5,5))[1],img.getpixel((5,5))[2])
    return colores
