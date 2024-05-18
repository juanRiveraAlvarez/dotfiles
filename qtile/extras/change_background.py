import json
import os
import sys
if len(sys.argv) == 2:
    route = sys.argv[1]
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir,'..','data','autostart.json')
    with open(json_file_path,'r+') as f:
        data = json.load(f)
        data["autostart"][0] = f'feh --bg-fill /home/juan/Pictures/{route} &'
    with open(json_file_path,'w') as f:
        json.dump(data,f,indent=4)
else:
    print("Ingrese ruta de forma  adecuada")
    
