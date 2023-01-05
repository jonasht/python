
#!/bin/bash

# Procura todos os diretórios .env e armazena o resultado em uma variável
DIRETORIOS=$(find . -type d -name ".env")

# Percorre a lista de diretórios encontrados e exclui cada um
for diretorio in $DIRETORIOS
do
  rm -r "$diretorio"
done
