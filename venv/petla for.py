lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

for litera in lista:
    print(litera)
    if litera == "e":
        print ("To jest e!")

print ("-----------------------------------")
# i to jakis random ktorego nie musimy okreslac
for i in range(10,30,2):# range generuje liste  od 0 do liczby w nawiasi eminus 1/ (50) --> 0...49
    print (i)# jesli (10,30 ) - wyswietli od 10 do 29
                # (10,30,2)- od 10 do 29 co 2