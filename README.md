# esses codigos foram feitos para meu portfolio

<hr>
os codigos começaram a ser feitos quando eu comecei a aprender programar em python,
por isso alguns podem parecer basicos  e outros podem ser complexos.
os programas estao dividos em pastas, cada pasta tem um programa.
<hr>
alguns codes podem precisar de bibliotecas para poder funcionar
a maioria dos codigos foram programados no gnu/linux Manajaro (Arch), 
alguns alguns codigos executados no windows podem não funcionar sem as biblitecas especificas 
ou pela configuraça.

<hr>
## (é necessario que o python 3 ja esteja instalado, caso seja linux é necessario que o pip esteja instalado)

## para fazer um ambiente de python primeiro deve instalar o virtualenv

```bash
pip install virtualenv
```

para fazer o ambiente deve usar:

```
python -m venv .env
```

(algumas distro linux usa-se python3 no lugar de python)

<hr>

## cada pasta tem seu requirements.txt

para instalar as bibliotecas
use:

```bash
pip install -r requirements.txt
```

## para ativar o virtual env na distro linux

```bash
source .env/bin/activate
```
