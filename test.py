from lxml.html import builder as E
from lxml.html import tostring

print (E,'...heloo')
html = E.HTML()
body = E.BODY()
html.append(body)
print (tostring(html))