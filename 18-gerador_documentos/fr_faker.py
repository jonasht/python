import pyperclip as pc


msg_str = 'o mundo vai acabar se o M0lusc0 ver as dicas do Peter (q fala que o bolsonaro ñ fez). e mandar o EXEs1to dar o G4LoP5, se ñ obedecer, "ele" manda embora '
binary_converted = ''.join(format(ord(c), "b") for c in msg_str)

# print(ord(msg_str))
print(binary_converted)
pc.copy(binary_converted)

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
X = msg_str
print(chr(bin(X[:8])))