# HTML Parser - Part 2
# https://www.hackerrank.com/challenges/html-parser-part-2/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print ('>>> Multi-line Comment', data, sep = '\n')
        else:
            print ('>>> Single-line Comment', data, sep = '\n')
    def handle_data(self, data):
        if data != '\n':
            print ('>>> Data', data, sep = '\n')

            
html = ''       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()