import urllib
import xml.etree.ElementTree as ET


#url = ' http://python-data.dr-chuck.net/comments_184402.xml'
#url = ' http://python-data.dr-chuck.net/comments_42.xml'
url = raw_input('Enter location: ')
###

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print data
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

aList = sum(int(c.text) for c in tree.findall('.//count'))

count = 0
for elem in tree.iter(tag='count'):
        count += 1

print "Sum: ", aList

print "Count: ", count

