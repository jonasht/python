import sqlite3
import json


class Maquina:
    def __init__(self, nomeMaquina):
        self.nomeMaquina = nomeMaquina

        
        self.nomeArquivo = self.nomeMaquina + '.json'


    def set_data(self, variableName, type, value):
        dados = []

        dado = {'variable': variableName, 'type': type, 'value': value}
        dados.append(dado)
        
    
        self.record_data(dados)


    # gravar dados
    def record_data(self, dados):
        dados = {self.nomeMaquina: dados}

        with open(self.nomeArquivo, 'w') as f_obj:
            json.dump(dados, f_obj)



    def update_data(self, variable, type, value):
        dados = []

        dados = self.get_data()
        dados = json.loads(dados)
        dados = dados[self.nomeMaquina]
        
        
        novoDado = {'variable': variable, 'type': type, 'value': value}
        dados.append(novoDado)

        self.record_data(dados)

        
    def get_data(self):
        with open(self.nomeArquivo) as f:
            dados = json.load(f)
        

        dados_json= json.dumps(dados)
        return dados_json

    def add_intoDB(self, ip=None, url=None):
        banco = sqlite3.connect('bancoDeDados.db')
        cursor = banco.cursor()

        cursor.execute("""
                        INSERT INTO (name, ip, url) VALUES(?, ?, ?)
                       """, (self.nomeMaquina, ip, url))
        banco.commit()
        banco.close()
        
if __name__ == '__main__':
    m = Maquina('m')
    m.set_data(variableName='teste', type='int', value=50)
    print(m.get_data())
    m.set_data(variableName='teste2', type='int', value=80)
    print(m.get_data())
    
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    m.update_data('teste3', 'str', 'umaPalavra')
    print(m.get_data())


