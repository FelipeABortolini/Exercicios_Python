import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[;31mErro ao abrir o site!\033[m')
else:
    print('\033[;33mSite aberto com sucesso!\033[m')
    print(site.read())
