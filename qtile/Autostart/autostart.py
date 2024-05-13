import json
import os
import psutil
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir,'..','data','autostart.json')
procesos = []
data={}
for i in psutil.process_iter(['pid','name']):
    procesos.append(i.info['name'])
    with open(json_file_path,'r') as  f:
        data = json.load(f)
for x in data['autostart']:
    name = x[:-2]
    if name not in procesos:
        os.system(x)

