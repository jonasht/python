#!/bin/bash

echo "procurando diretorios"
# Procura todos os diretórios .env e armazena o resultado em uma variável
DIRETORIOS=$(find . -type d -name ".env")

# Percorre a lista de diretórios encontrados e exclui cada um
echo "removendo: "
for diretorio in $DIRETORIOS; do
  echo "$diretorio"
  rm -r "$diretorio"

done

echo "procurando diretorios"
# Procura todos os diretórios .env e armazena o resultado em uma variável
DIRETORIOS=$(find . -type d -name "__pycache__")

# Percorre a lista de diretórios encontrados e exclui cada um
echo "removendo: "
for diretorio in $DIRETORIOS; do
  echo "$diretorio"
  rm -r "$diretorio"

done

echo "procurando diretorios"
# Procura todos os diretórios .env e armazena o resultado em uma variável
DIRETORIOS=$(find . -type d -name ".vscode")

# Percorre a lista de diretórios encontrados e exclui cada um
echo "removendo: "
for diretorio in $DIRETORIOS; do
  echo "$diretorio"
  rm -r "$diretorio"

done
