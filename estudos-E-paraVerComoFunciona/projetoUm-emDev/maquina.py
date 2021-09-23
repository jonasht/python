
import json


class Maquina:
    def __init__(self, nomeMaquina):
        self.nomeMaquina = nomeMaquina
        
        self.dados = []

    def set_data(self, variableName, type, value):
        

        dados = {'variable': variableName, 'type': type, 'value': value}
        self.dados.append(dados)
    
    def get_data(self):
        data = {self.nomeMaquina: self.dados}
        data_json = json.dumps(data)
        return data_json


if __name__ == '__main__':
    m = Maquina('m')
    m.set_data(variableName='teste', type='int', value=50)
    print(m.dados)

    print()
    print(m.get_data())

    m.set_data(variableName='teste2', type='char', value='caracter')
    print(m.get_data())

