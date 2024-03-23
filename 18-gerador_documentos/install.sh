echo "funciona arch linux"
echo "pode nao funcionar corretamento em outros OS"

# xclip serve para pyperclip funcionar e tk serve para tkinter funcionar
echo "instalando xclip e tk"
sudo pacman -S xclip tk

echo "criando env e instalando pacotes"
python -m venv .env
source .env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "instalacao feita com sucesso" 
