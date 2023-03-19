echo "funciona arch linux"
echo "instalando xclip e tk"
sudo pacman -S xclip tk

echo "criando env e instalando pacotes"
python -m venv .env
source .env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
