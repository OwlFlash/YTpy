"""import foo # importujesz stworzony przez cb moduł 0plik foo)

print("Hello world") # bardzo istotne jest ze musizz ddac foo. i nazwe funkcji
foo.test("Bar")
foo.test("world")
foo.apple("iphone")"""

"""from foo import test, apple# nie musisz całego modułu importować- możesz też tylko funkcje

test("Bar") # już nie dajesz foo.test tylko samo test
apple("mac")"""

"""# 1 spodob :
import time
print("a")
time.sleep (2)
print("b")

#2 sposob

from time import sleep
print("a")
sleep(2)
print("b")"""



"""from foo import * # importuj wszytsko z modułu(każdą funkcje)

test("Hello")
apple("drzewo")
"""
def cos ():
    print("Cos z run")

"""cos() # teraz masz w pliku dwie funkcje 'cos' 1. z pliku run a druga zaimportowana z foo
# zostanie wyswietlona funkcja ktora zostala ostatnio zadeklarowana lub zaimportowana"""

from foo import cos as cos_foo

cos()
cos_foo()

