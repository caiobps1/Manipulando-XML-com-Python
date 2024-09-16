# Script de limpeza para arquivo XML



Para automatizar a tarefa de excluir as tags com problema utilizei a biblioteca xml.etree.ElementTree do Python para processar o meu arquivo XML

O arquivo XML possui uma tag chamada <spawn> e é repetida ao longo de mais de 20mil linhas. Algumas tags no arquivo estão com problema e estão vazias, por isso precisam ser removidas.


O método findall('monster') é utilizado para buscar todas as tags <monster> dentro de cada <spawn>. Se a lista estiver vazia (if not monsters:), a tag <spawn> é removida do XML.

Após fazer as alterações, o arquivo corrigido é salvo como arquivo_corrigido.xml.
