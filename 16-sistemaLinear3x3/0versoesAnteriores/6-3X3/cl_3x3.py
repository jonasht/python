
# calculo linear 3x3
# regra de cramer
# --------------------------------------------------

class cl_3x3:
    
    def __init__(self,conta):
        self.conta = conta
        self.matriz_delta = self.get_matrizMontada()
        self.matriz_deltaX = self.get_matrizMontada('x')
        self.matriz_deltaY = self.get_matrizMontada('y')
        self.matriz_deltaZ = self.get_matrizMontada('z')
        

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


    def get_matrizMontada(self, op='='):
        matriz = [[], [], []]
        
        if op == '=':
            for i, dic in enumerate(self.conta):
                for chave, item in dic.items():
                    if chave != '=':
                        matriz[i].append(item)
                        
        else:
            for i, dic in enumerate(self.conta):
                for chave, item in dic.items():
                    if chave != '=':                
                        if chave == op:
                            matriz[i].append(self.conta[i]['='])
                        else:
                            matriz[i].append(item)                    
                            
        for i in range(3):
            for ii in range(2):
                matriz[i].append(matriz[i][ii])
        return matriz



    def mostrar_matriz(self, matriz):
        
        for lista in matriz:
            for n in lista:
                if len(str(n)) == 1:
                    print(f'  {n}', end='')
                else:
                    print(f' {n}', end='')
            print()


    def somarMatriz(self, matriz):
        
        multiplicacao = 1
        resultado = 0
        for seguinte in range(3):
            for i in range(3):
                multiplicacao *= matriz[i][i+seguinte]
            resultado += multiplicacao
            multiplicacao = 1
                
        for seguinte in range(3):
            for i in range(3):            
                multiplicacao *= -(matriz[-(i-2)][i+seguinte])
            resultado += multiplicacao
            multiplicacao = 1

            
        return resultado

