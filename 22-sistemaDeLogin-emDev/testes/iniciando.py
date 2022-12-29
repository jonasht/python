import os 



data = os.listdir()
print(data)

if 'db.sqlite' not in data:
    print('nao esta')

else:
    print('esta')