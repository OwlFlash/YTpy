# TUPLE SA WYDAJNIEJSZE OD LIST , BO NIE MOZNA ICH EDYTOWac
#zamiast [] dajesz ()
#produkty = ("mleko", "ser", "cola")
# w funkcjach masz tylko policz i indeks wypisz czyli tylko takie funkcje ktore nie wprowadzaja zmian a daja informacje


# słownik - zestaw kluczy i wartości. daje sie {}
person = {"wiek" : 20, "imię" : "Ania", "nazwisko" : "Kowalska"} # : wiek - klucz  20 - wartosc
print (person)
print(type(person))# dic - dictionary
print(person["wiek"])
# print (person [0]) - wyskoczy error bo w odrozznienu do tupli i list nie segregujemy elementow po indeksach a po kluczach ktore sami ustalamy np. "wiek"
print(person["nazwisko"])
# Funkcje słownika
#get -dziala dokladnie jak person["wiek"] ale jesli nie znajdzie takiego klucza to mozemy wymusic zeby wyswietlił daną wartośc
#keys - lista kluczy
#varus - lista wartosci
#itenms - lista tupli

print(person.get("wzrost",25))# wyswietli 25 bo nie ma klucza "wzrost"