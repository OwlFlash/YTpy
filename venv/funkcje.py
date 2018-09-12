# FUNKCJA - CZESC KODU KTORY SPELNIA DANE ZADANIE
def printme() : # funkcje musza miec rozn enazwy. define -def
    print("HELLO") # po wcieciu dajesz to co ma sie wykonac po wywolaniu takiej funkcji
    print ("World")
printme() # na gorze ja tylko definiowalas. teraz musisz ja normalnie wywołac
print("________________________________________________")

def printmoi(liczba) :# w () 'ciele' - argumenty
    print ( "Test :", end = '') # nie przelamuje nam. pisze w jednej linijce
    print (liczba)

printmoi(5)

print("_________________________________")

def mnoz(a,b=4):
    print(a*b)

mnoz(2,2)
mnoz(3) # b jest opcjonalne. jesli nic tu nie wpiszemy to wezmie 'b' z def -domyślne- a jesli wpiszemy to wezmie nasze
mnoz(3,9)

print("________________________-")

def odejmuj(a,b):
    return a-b
wynik = odejmuj (4,4)
x = odejmuj(b=3, a =1)
print(wynik)
print(x)

print("___________________________________")

def dodaj (a=4,b=1,c=3):
    return a+b+c
k = dodaj(2, c =0)
print(k)


