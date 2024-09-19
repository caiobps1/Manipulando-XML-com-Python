import argparse
import re

def corrigir_xml(arquivo_xml):
    with open(arquivo_xml, 'r', encoding='utf-8') as file:
        conteudo = file.read()
        conteudo = conteudo.replace('chance1', 'chance')
        conteudo = re.sub(r' countmax="\d+"', '', conteudo)
        conteudo = re.sub(r'--\s?(.*?)\s*(?=<)', r'<!-- \1 -->\n', conteudo)
        
    with open(arquivo_xml, 'w', encoding='utf-8') as file:
        file.write(conteudo)
        print(f'{arquivo_xml} corrigido.')

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Corrigir arquivo XML de loot.")
        parser.add_argument("caminho_arquivo", help="Caminho do arquivo XML a ser corrigido")
        args = parser.parse_args()
        corrigir_xml(args.caminho_arquivo)
