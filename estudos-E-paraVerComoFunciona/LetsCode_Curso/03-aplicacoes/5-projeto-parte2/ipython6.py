# coding: utf-8
get_ipython().run_line_magic('run', '5.py')
dados
def get_dataSets(y, labels):
    if type(y[0]) == list:
        datasets = []
        
        for i in range(len(y)):
            datasets.append({
            'label': labels[i],
            'data': y[i]
            })
            return datesets
        else:
        return [
        {
            'label': labels[0],
            'data': y
        }
        ]    
def get_dataSets(y, labels):
    if type(y[0]) == list:
        datasets = []
        
        for i in range(len(y)):
            datasets.append({
            'label': labels[i],
            'data': y[i]
            })
            return datasets 
    else:
        return [
        {
            'label': labels[0],
            'data': y
        }
        ]
            
def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
        }
        
def create(x, y, labes, kind='bar', title=''):
    datasets = get_dataSets(y, labels)
    options = set_title(title)
    
    chart = {
        'type': kind,
        'data': {
                'labels': x,
                'datasets': datasets
                },
                'options': options
                }

def get_api_chart(chart):
   url_base = 'https://quickchart.io/chart'
   resp = r.get(f'{url_base}?c={str(chart)}')
   return resp.content
  
def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)
        
from PIL import Image
from IPython.display import display
def display_image(path):
    img_pil = Image(path)
    display(img_pil)
    
y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
    
y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])
    
labels = ['confirmados', 'recuperados]
def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)
    
y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
    
y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])
    
labels = ['confirmados', 'recuperados]
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
    
y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])
    
labels = ['confirmados', 'recuperados']

x = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
    
y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])
    
labels = ['confirmados', 'recuperados']

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d%m%Y'))

chart = create_chart(x, [y_data_1, y_data_2], labels, title='grafico confirmados vs recuperados')
chart_content = get_api_chart(chart)
save_image('meuprimeirografico.png', chart_content)
display_image('meuprimeirografico.pgn')
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
    
y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])
    
labels = ['confirmados', 'recuperados']

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d%m%Y'))

chart = create_chart(x, [y_data_1, y_data_2], labels, title='grafico confirmados vs recuperados')
chart_content = get_api_chart(chart)
save_image('meuprimeirografico.png', chart_content)
display_image('meuprimeirografico.pgn')
def create_chart(x, y, labes, kind='bar', title=''):
    datasets = get_dataSets(y, labels)
    options = set_title(title)
    
    chart = {
        'type': kind,
        'data': {
                'labels': x,
                'datasets': datasets
                },
                'options': options
                }
                
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
    
y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])
    
labels = ['confirmados', 'recuperados']

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d%m%Y'))

chart = create_chart(x, [y_data_1, y_data_2], labels, title='grafico confirmados vs recuperados')
chart_content = get_api_chart(chart)
save_image('meuprimeirografico.png', chart_content)
display_image('meuprimeirografico.pgn')
get_ipython().run_line_magic('save', 'ipython6 1-26')
