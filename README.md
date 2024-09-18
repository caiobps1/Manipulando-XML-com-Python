# Manipulando XML com Python

## Excluir tags com estrutura irregular (limpar.py)
Para automatizar a tarefa de excluir as tags com problema utilizei a biblioteca **xml.etree.ElementTree** do Python para processar o meu arquivo XML

O arquivo XML possui uma tag chamada <spawn> e é repetida ao longo de mais de 20mil linhas. Algumas tags no arquivo estão com problema e estão vazias, por isso precisam ser removidas.

> Note que na linha 8 a tag está vazia. Ela precisa ser removida.
```
<?xml version="1.0"?>
<spawns>
	<spawn centerx="360" centery="218" centerz="0" radius="5">
		<monster name="Lizard Chosen" x="0" y="-2" z="0" spawntime="120" />
		<monster name="Juggernaut" x="3" y="0" z="0" spawntime="120" />
		<monster name="Lizard Zaogun" x="-2" y="1" z="0" spawntime="120" />
	</spawn>
	<spawn centerx="367" centery="218" centerz="0" radius="5" />
	<spawn centerx="328" centery="248" centerz="0" radius="5">
		<monster name="Lizard Chosen" x="-1" y="-3" z="0" spawntime="120" />
		<monster name="Lizard High Guard" x="3" y="-1" z="0" spawntime="120" />
		<monster name="Lizard High Guard" x="-2" y="1" z="0" spawntime="120" />
	</spawn>
	<spawn centerx="357" centery="248" centerz="0" radius="5">
		<monster name="Lizard Chosen" x="1" y="-3" z="0" spawntime="120" />
		<monster name="Lizard Legionnaire" x="-1" y="-1" z="0" spawntime="120" />
		<monster name="Lizard Zaogun" x="3" y="-1" z="0" spawntime="120" />
	</spawn>
```

O método findall('monster') é utilizado para buscar todas as tags <monster> dentro de cada <spawn> . Se a lista estiver vazia _(if not monsters:)_, a tag <spawn> é removida do XML.

Após fazer as alterações, o arquivo corrigido é salvo como arquivo_corrigido.xml.


## Excluir tag e ajustar comentários (corrigir-xml.py)

A estrutura do meu arquivo possui a seguinte linha:

```<item id="2463" countmax="1" chance1="800" chancemax="10000" /> -- plate armor```

Preciso verificar cada linha do arquivo e modificar a tag ```chance1``` para ```chance``` e remover a tag ```chancemax```.

Além disso preciso alterar o comentário ```-- plate armor``` para ```<!-- plate armor -->```

Ajustei o script para ser chamado por linha de comando utilizando a biblioteca argparse para processar os argumentos.

Comando para executar arquivo ``` python corrigir_xml.py arquivo.xml ```

Eu utilizei python3 em uma máquina linux

