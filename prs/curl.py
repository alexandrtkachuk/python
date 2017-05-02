import pycurl
from io import StringIO, BytesIO
from lxml import etree
from pprint import pprint

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://pycurl.io/')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.

tree = tree = etree.HTML( body.decode('utf-8') )
nodes = tree.xpath('//h2')
print('найдно h2: ',  len(nodes));
for node in nodes:
    print(node.text)
#print()
