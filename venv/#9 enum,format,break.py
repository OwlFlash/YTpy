fruits = [ 'apple', 'orange', 'pear', 'banana', 'apple']

print("Start")
for i, fruit in enumerate(fruits) :# dzieki funkcji enumerate petla for przyjmuje 2 arg. dla kazdego indeksu "i" do elementu ktory odczytujemy w liscie chcemy wypisac owoc i to "i"
    if i == 3 :
        break
    print(i)# przed przecinkiem numer elementu, po przecinku elemnet ktory odczytujemy
    print (fruit)
print("Koniec")
print("-------------------------------------------")

#format -  podobne do tego co robilismy na poczatku po kropce. funkcja do stringów tym razem

vegetables = ["potato", "onion", "tomato", "carrot"]

print("Start")
for x, vegetable in enumerate(vegetables) :
    print ("Sprawdzam {}" .format(x))# w miejsu {} zostaje wypisane to(zmienna?) z ()
    if  x == 3 :
        break
    print ("{} jest ok".format(vegetable))
    print (vegetable)
print("Koniec")

print("____________________________________________________")

for fruit in fruits:

    if fruit == "orange" :continue # orange nie zostanie wyswietlone, continue pomija orange i jedzie dalej tzn. reszta kodu po orange zostaje pominieta (to z break) i wraca na poczatek
    if fruit == "banana": break # jesli mamy jedna funkcje to mozemyt tak zapisac break i continue po if
    print(fruit)

print("_______________________________________________")
fruits = [ 'apple', 'orange', 'pear', 'banana', 'apple', 'strawberry', 'apple', 'blueberry']

if "apple" in fruits:
    print ("Znaleziono jabłko")
elif "orange"  in fruits:  # else if
    print ("Nie znaleziono jabłka, ale mamy pomarańczę")
else : print("Nic nie znaleziono")