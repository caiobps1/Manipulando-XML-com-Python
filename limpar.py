import xml.etree.ElementTree as ET

tree = ET.parse('spawn-sem-limpeza.xml')
root = tree.getroot()

for spawn in root.findall('spawn'):
    monsters = spawn.findall('monster')
    if not monsters:
        root.remove(spawn)

tree.write('spawn-limpo.xml')