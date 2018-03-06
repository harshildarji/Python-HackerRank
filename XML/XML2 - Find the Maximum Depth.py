# XML2 - Find the Maximum Depth
# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem

import xml.etree.ElementTree as etree

def goDeeper(depth, node):
    if len(node)>0:   
        depth = max(goDeeper(depth + 1, x) for x in node)
    return depth

xml = ''.join(input() for _ in range(int(input())))
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()

print(goDeeper(0, root))
