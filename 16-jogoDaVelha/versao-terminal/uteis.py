

# verificar se o X ou O ganhou returnando verdadeiro, matriz = eh jogo da velha
def verificar(char, matriz):
    # char = caracter para X ou O ou outro que quiser pode verificar se ganhou
    # 0 --- posicao
    if matriz[0][0] == char and matriz[0][1] == char and matriz[0][2] == char:
        return True
    
    # 1 --- posicao
    elif matriz[1][0] == char and matriz[1][1] == char and matriz[1][2] == char:
        return True

    # 2 --- posicao
    elif matriz[2][0] == char and matriz[2][1] == char and matriz[2][2] == char:
        return True
    
    # 0 |   posicao
    elif matriz[0][0] == char and matriz[1][0] == char and matriz[2][0] == char:
        return True 
    # 1 |
    elif matriz[0][1] == char and matriz[1][1] == char and matriz[2][1] == char:
        return True   
    # 2 |   posicao
    elif matriz[0][2] == char and matriz[1][2] == char and matriz[2][2] == char:
        return True         
    # \     posicao
    elif matriz[0][0] == char and matriz[1][1] == char and matriz[2][2] == char:
        return True 
    # /     posicao
    elif matriz[2][0] == char and matriz[1][1] == char and matriz[0][2] == char:
        return True 
    else:
        return False
