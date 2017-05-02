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
#print(body);
temp = etree.fromstring(body)
etree.tostring(temp)
nodes = etree.parse('//h2')
print(len(nodes));
#print()
