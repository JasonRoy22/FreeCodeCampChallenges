import re
import socket
import urllib.request
import json


"""width = 15
height = 12.0
print(height/3)
print(type(height))
print (10 / 2)

nam = input('Who are you? ')
print('Welcome', nam)
"""
"""inp = input('Europe floor ')
usf = int(inp) + 1
print("US floor", usf)"""

"""def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()"""

"""n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1"""


"""for i in [2,1,5]:
    print(i)"""
"""
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break # breaks the code
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)"""

"""0 == 0.0
0 is 0.0  #false
0 is not 0.0
0 = 0.0"""

"""for n in "banana":
    print(n)"""

"""word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)"""
"""
word = "bananana"
i = word.find("na")
print(i)
"""

"""fruit = "banana"
x = fruit[1]
print(x)"""

"""words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
print(n)"""

"""dict = {"Fri": 20, "Thu": 6, "Sat": 1}
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9
print(dict)"""

"""
counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))
"""

"""counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])"""

"""d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)"""

"""lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)
"""

"""for line in hand:
    line = line.rstrip()
    if re.search('^From', line):
        print(line)"""


"""s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)"""


"""mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()"""

"""fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())"""

"""
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])"""

"""class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()
"""

"""class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()"""

