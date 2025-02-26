import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=HQcEDB8Pfeg&list=RDMM&index=7&pp=8AUB')
except urllib.error:
    print("o cuble dos canalhas esta fechado :(")
else:
    print("o cuble dos canalhas esta aberto :)")
