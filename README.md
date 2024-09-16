# Script de limpeza para arquivo XML



Para automatizar a tarefa de excluir as tags com problema utilizei a biblioteca xml.etree.ElementTree do Python para processar o meu arquivo XML

O arquivo XML possui uma tag chamada <spawn> e é repetida ao longo de mais de 20mil linhas. Algumas tags no arquivo estão com problema e estão vazias, por isso precisam ser removidas.

Exemplo de TAG correta:
	spawn centerx="877" centery="744" centerz="7" radius="1"
		monster name="Wolf" x="1" y="0" z="7" spawntime="60" /
	/spawn

Exemplo de TAG incorreta:
	spawn centerx="681" centery="744" centerz="7" radius="5" /

O método findall('monster') é utilizado para buscar todas as tags <monster> dentro de cada <spawn>. Se a lista estiver vazia (if not monsters:), a tag <spawn> é removida do XML.

Após fazer as alterações, o arquivo corrigido é salvo como arquivo_corrigido.xml.
