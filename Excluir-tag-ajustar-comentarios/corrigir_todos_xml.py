import argparse
import re
import os
import glob

def corrigir_xml(arquivo_xml):
    with open(arquivo_xml, 'r', encoding='utf-8') as file:
        conteudo = file.read()
    conteudo = conteudo.replace('chance1', 'chance')
    conteudo = re.sub(r' countmax="\d+"', '', conteudo)
    conteudo = re.sub(r'--\s?(.*?)\s*(?=<)', r'<!-- \1 -->\n', conteudo)
    with open(arquivo_xml, 'w', encoding='utf-8') as file:
        file.write(conteudo)
    print(f'{arquivo_xml} corrigido.')

def processar_diretorio(diretorio):
    arquivos_xml = glob.glob(os.path.join(diretorio, "**", "*.xml"), recursive=True)
    if not arquivos_xml:
        print(f'Nenhum arquivo .xml encontrado no diretório {diretorio}')
        return
    for arquivo in arquivos_xml:
        if os.path.basename(arquivo) == "monsters.xml":
            print(f'Ignorando o arquivo {arquivo}')
            continue       
        corrigir_xml(arquivo)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Corrigir todos os arquivos XML de um diretório e suas subpastas, exceto 'monsters.xml'.")
    parser.add_argument("caminho_diretorio", help="Caminho do diretório contendo os arquivos XML a serem corrigidos")
    args = parser.parse_args()
    processar_diretorio(args.caminho_diretorio)