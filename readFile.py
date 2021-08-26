import json
import time
a = 0
b = True

while b is True:
    t = open('teste.json',)
    teste = json.load(t)
    print(teste)
    time.sleep(1)
    a += 1
    if a >= 10:
        b = False
