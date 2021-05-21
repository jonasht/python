import json

class Db:
    def __init__(self):
        self.fileName = 'dados.json'
        
        # opcoes de cadastro
        self.id = str(1)
        self.nome = ''
        self.idade = ''
        # self.sexo
        
        
    def set_db(self, dados):
        with open(self.fileName, 'w') as file:
            json.dump(dados, file)
    
    def get_db(self):
        with open(self.fileName) as file:
            db = json.load(file)
        return db
    
    def update_db(self, dados):
        try:
            db = self.get_db()
            db.update(dados)
            self.set_db(db)
        except:
            self.set_db(dados)
    
    def mostrar(self):
        db = self.get_db()
        for id, dados in db.items():
            print('id:', id, 'dados:', dados)
    
    def cadastrar(self):
        self.id = str(len(self.get_db()) + 1)
        dados ={self.id: dict(
            nome=self.nome,
            idade=self.idade,
        )}
        self.update_db(dados)


if __name__ == '__main__':        
    db = Db()
    db.mostrar()
    print(len(db.get_db()))

