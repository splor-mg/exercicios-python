import argparse
from pathlib import Path

parser = argparse.ArgumentParser()


parser.add_argument("caminho_pasta")
args = parser.parse_args()
# print(args.nome_arquivo, args.caminho_pasta)

caminho_pasta = Path(args.caminho_pasta)
if not caminho_pasta.parent.is_dir(): 
    print(f'{caminho_pasta.parent} não é um caminho válido.')
else:
    caminho_pasta.mkdir()
    (caminho_pasta / '_README.md').touch()
    (caminho_pasta / 'main.py').touch()
    (caminho_pasta / '__init__.py').touch()
    pasta_testes = caminho_pasta / 'tests'
    pasta_testes.mkdir()
    (pasta_testes/ '__init__.py').touch()
    (pasta_testes/ 'test_.py').touch()
    