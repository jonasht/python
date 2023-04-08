

def read(path):
    with open(path, 'r') as reader:
        text = reader.read()
        return text


def write(path, text):
    with open(path, 'w') as writer:
        writer.write(text)

        


if __name__ == "__main__":
    write('text.txt', 'hello world')

    print(read('./text.txt'))

        