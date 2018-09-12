import time # nie mamy tego modułu. musimy go zaiportować

#print("Start")
#time.sleep(2) # stop zostanie wyswietlony po 2 sec. Program zostal zatrzymany na 2 s/ rzadko korzystamy- malo efektywne bo caly program si ezatrzymuje
#print("Stop")

"""print(time.time())# zwraca "unixowy" ? czas - ile sec mineło od 01.01.1970 r / tak komp liczy daty
timer = time.time()
time.sleep(2)
elapsed = time.time() - timer
print(elapsed) # powinno wyjsc 2 - roznica miedzy czasem jak rozpoczniemy program i jak sie znowu uruchomi po tych 2 s
"""

"""timer = time.time()
timer2 = time.time()
while True :
    if time.time() - timer > 2 : #sprawdzamy czy minely wiecej niz 2 sec od ustalenia timera
        print("2 sekundy")
        timer = time.time()# resetujemy timer, zeby znowu zaczelo odliczac od nowa te 2 sec. Wyświetlaja sie 2 sec co 2 sec- gdybysmy to pomineli (ten reset) to ciagle by si ewyswietlaly te 2 sec w nieskonczonosc (czesciej niz co 2 sec)

    if time.time( )- timer2 > 1 :
        print("1 sec")
        timer2 = time.time()
"""
import datetime

teraz = datetime.datetime.now()

print(str(teraz.hour)+ ":" + str(teraz.minute))


print(teraz.strftime("%H:%M %d.%m.%Y")) # WAŻNA - całkiem przydatna - w systemie 12-godzinnym H zamieniamy na I--
print(teraz.strftime("%I:%M %p %d.%b.%Y")) #B - caly nazwa miesiaca