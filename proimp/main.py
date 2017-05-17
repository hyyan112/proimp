# coding=utf-8
import json
import os
import re
import sys

from proimp.model import Module, Edge

excludes = ['venv', '__pycache__']
_from_import = re.compile('from\s(.*)\simport\s(.*)')
# _import = re.compile('import\s(.*)')

edges = {}
modules = {}
root = ''


def find(py_file):
    with open(py_file, encoding='utf-8') as f:
        r = f.read()
    fi = _from_import.findall(r)
    source = py_file.split(root)[1].replace('/', '.').replace('.', '', 1).replace('.py', '')
    for i in fi:
        target, child = i
        children = set(child.replace('(', '').replace(')', '').replace('\\', '').split(','))
        key = '{}-{}'.format(source, target)
        if key not in edges:
            e = Edge(source=source, target=target)
            edges[key] = e
        if target not in modules:
            m = Module(label=target, size=len(children))
            modules[target] = m
        else:
            modules[target].accumulate(len(children))


def loop(my_root):
    filelist = os.listdir(my_root)
    for i in filelist:
        if i not in excludes:
            subfile = os.path.join(my_root, i)
            if os.path.isdir(subfile):
                loop(subfile)
            elif i.endswith('py'):
                find(subfile)


def main():
    r = sys.argv[1]
    global root
    root = r
    loop(r)
    data_edg = []
    data_mod = []
    data = {}
    for k, v in edges.items():
        data_edg.append(v.to_json())
    data['edges'] = data_edg
    for k, v in modules.items():
        data_mod.append(v.to_json())
    data['nodes'] = data_mod
    with open('./templates/dependencies.html', encoding='utf-8') as f:
        l = f.read()
        d = json.dumps(data)
        r = l.replace('{{results}}', d)
    with open('./output.html', 'w+', encoding='utf-8') as f:
        f.write(r)


if __name__ == '__main__':
    main()
