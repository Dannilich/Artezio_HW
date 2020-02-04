"""
Задание 4:

На вход функции передается строка с xml документом (тэги без аттрибутов, корневой элемент только один).
Нужно выполнить следующее преобразование и вывести максимальную вложенность.

Пример:
        a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
        foo(a) ->
        {
            'name': 'root',
            'children': [
                {'name': 'element1', 'children': []},
                {'name': 'element2', 'children': []},
                {
                    'name': 'element3',
                    'children': [
                        {'name': 'element4', 'children': []}
                    ]
                }
            ]
        }, 2
в данном случае у element4 тэга вложенность/глубина 2
"""
! не реализованно
import xml.etree.ElementTree as  xml_tree

xml_str = \
    """
    <?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
    """
tree = xml_tree.parse("source.xml")
print(tree.getroot())
#print(xml_tree.fromstring(xml_str))
iter_ = tree.getiterator()

for elem in iter_:
    print(elem.tag)

print("-" * 40)
print("Обрабатываем дочерние жлменты getchildren()")
print("-" * 40)
appointments = tree.getroot().getchildren()

for appointment in appointments:
    appt_children = appointment.getchildren()
    for appt_child in appt_children:
        print("%s=%s" % (appt_child.tag, appt_child.text))

print("*"*50)
print(len(tree.getroot().getchildren()))

for num_of_line in tree.getroot().getchildren():
    print(len(num_of_line.getchildren()))