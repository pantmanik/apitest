import urllib.parse

url='https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg'

urlu=urllib.parse.unquote(url)
print(urlu)
urlq=urllib.parse.quote(url)
print(urlq)

path=urllib.parse.urlparse(urlu).path
print(path)
pathq=urllib.parse.quote(path)
print(pathq)
netloc=urllib.parse.urlparse(urlu).netloc
print(netloc)
# print(urllib.parse.urlparse(urlu))
scheme=urllib.parse.urlparse(urlu).scheme
print(scheme)
finurl=urllib.parse.urlunparse((scheme,netloc,pathq,'','',''))
print(finurl)