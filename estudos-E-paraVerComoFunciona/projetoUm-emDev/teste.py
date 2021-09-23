import json 

variableName = 'algo'
type = 'str'
value = 'uma Palavra'


data = {'variable_name': variableName, 'type': type, 'value': value}
data = json.dumps(data)
print(data)

# data_json = json.loads(data)
