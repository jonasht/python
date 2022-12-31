
echo "upgrade pip"
pip install --upgrade pip

echo "update libs pip"
pip install -U $(pip freeze | awk '{split($0, a, "=="); print a[1]}')