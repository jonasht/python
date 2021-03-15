
# calculo linear
# regra de cramer

class cl_3x3:

    def __init__(self, conta):
        self.conta = conta
        
        self.matriz = [[], [], []]
        
    def mostrar_conta(self):

        for dic in self.conta:
            for chave, item in dic.items():
                if chave == '=':
                    print(f' = {item}', end='')
                else:
                    if len(str(item)) == 1:
                        print(f'  {item}{chave}', end='')
                    else:
                        print(f' {item}{chave}', end='')
            print()
            

    def get_matrizMontada(self, opcao='='):

        if opcao == '=':
            for i, dic in enumerate(self.conta):
                for chave, item in dic.items():
                    if chave != '=':
                        self.matriz[i].append(item)

        else:
            for i, dic in enumerate(self.conta):
                for chave, item in dic.items():
                    if chave != '=':
                        if chave == opcao:
                            self.matriz[i].append(self.conta[i]['='])
                        else:
                            self.matriz[i].append(item)

        for i in range(3):
            for ii in range(2):
                self.matriz[i].append(self.matriz[i][ii])
        

        return self.matriz


    
    def mostrar_matriz(self):

        
        for lista in self.matriz:
            for n in lista:
                if len(str(n)) == 1:
                    print(f'  {n}', end='')
                else:
                    print(f' {n}', end='')
            print()


    def somarMatriz(self):
        
        multiplicacao = 1
        resultado = 0
        for seguinte in range(3):
            for i in range(3):
                multiplicacao *= self.matriz[i][i+seguinte]
            resultado += multiplicacao
            multiplicacao = 1

        for seguinte in range(3):
            for i in range(3):
                multiplicacao *= -(self.matriz[-(i-2)][i+seguinte])
            resultado += multiplicacao
            multiplicacao = 1

        return resultado

