import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir,'..','data','gruvbox.json')
with open(json_file_path,'r') as  f:
    data = json.load(f)
def color_bar():
    colores = data['colores']
    return colores
