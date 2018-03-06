# XML 1 - Find the Score
# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem

import xml.etree.ElementTree as etree
xml = ''.join(input() for _ in range(int(input())))
tree = etree.ElementTree(etree.fromstring(xml))

def traverse(node):
  return etree.tostring(node).count(b'=')

print(traverse(tree.getroot()))
