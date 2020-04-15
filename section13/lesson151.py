"""
XML
古いデータ送信形式
<?xml version='1.0' encoding='utf-8' ?>
<root>
    <employee>
        <employ>
            <id>111</id>
            <name>Mike</name>
        </employ>
        <employ>
            <id>222</id>
            <name>Nancy</name>
        </employ>
    </employee>
</root>
"""

import xml.etree.ElementTree as ET

# <root></root>の作成
root = ET.Element('root')

# rootに情報を付け加える
tree = ET.ElementTree(element=root)

# rootの中の階層を追加
employee = ET.SubElement(root, 'employee')

# データの追加
employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '111'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = 'Mike'

# データの追加
employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '222'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = 'Nancy'

# XMLファイルの書き込み
tree.write('test.xml', encoding='utf-8', xml_declaration=True)

# XMLファイルの読み込み
tree = ET.ElementTree(file='test.xml')
root = tree.getroot()

# データの取り出し(forループを使う)
for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag, person.text)
