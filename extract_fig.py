import json
import base64

with open('./histograms.ipynb', 'r') as f:
    data = json.load(f)

xx = [
    cell
    for cell in data['cells']
    if 'indicate_inset_zoom' in ''.join(cell['source'])
]
for output in xx[0]['outputs']:
    if output['output_type'] == 'display_data':
        png = output['data']['image/png']
        break
else:
    raise Exception('cannot find display_data')

with open('figures/distance_between_stops.png', 'wb') as f:
    f.write(base64.b64decode(png))
