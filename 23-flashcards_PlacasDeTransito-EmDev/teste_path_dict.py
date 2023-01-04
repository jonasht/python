from readDir import read_dir
from nomePlacasList import nomePlaca



print(read_dir()[:5])
print('==========')

placas_keys = nomePlaca.keys()
placas_keys = list(placas_keys)[:5]

for p in placas_keys:
    print(p)

