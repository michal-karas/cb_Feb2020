# dodanie obsługi plików CSV
import csv


data = []

# otwarcie pliku
with open("c:/Users/User/Desktop/Python/03_Python/zadanie domowe/przykladowy.csv", "r") as f:
    # DictReader pozwoli odczytywać dane z pliku CSV
    # i będzie je zwracał jako słowniki
    reader = csv.DictReader(f)

    # iterujemy po readerze
    for row in reader:
        # dokonujemy konwersji danych i dokładamy je na
        # koniec naszej listy
        data.append(
            {
                "year": int(row["Year"]),
                "score": int(row["Score"]),
                "title": row["Title"],
            }
        )

# ZADANIA:
# Znajdź tytuł najgorszego filmu Roberta de Niro
#    * Znajdź tytuły kilku najgorszych filmów
# Znajdź tytuł najlepszego filmu RdN
#    * Znajdź tytuły kilku najlepszego filmów
# Znajdź średnią ocen filmów RdN
# * Znajdź medianę ocen filmów RdN
# * Znajdź rok, w którym RdN wydał najwięcej filmów

#najgorszy film
worst_score = 100
worst_score = data[0]["score"]
for entry in data:
    if entry["score"] <= worst_score:
        worst_score = entry["score"]
        worst_title = entry["title"]

print(f"Najgorsza ocena filmu RdN to: {worst_score}")
print(f"Tytuł najgorszego filmu to {worst_title}")

#najlepszy film
best_score = 100
best_score = data[0]["score"]
for entry in data:
    if entry["score"] > best_score:
        best_score = entry["score"]
        best_title = entry["title"]

print(f"Najlepsza ocena filmu RdN to: {best_score}")
print(f"Tytuł najlepszego filmu to {best_title}")

#średnia
suma = 0
list_of_elements = 0
for entry in data:
    suma += entry["score"]
    list_of_elements += 1

print("Średnia ocen z wszytskich filmów Roberta to: ", suma / list_of_elements)

#mediana
mediana_list=[]
liczba_elementow = 0
for entry in data:
        worst_score = entry["score"]
        mediana_list.append(worst_score)
        liczba_elementow += 1

x = sorted(mediana_list)
print(x)
print ("Ilość liczb w tabeli to: ", liczba_elementow)
print ("wyznaczamy środek- tutaj zostanie podana cyfra środka ciągu : ", liczba_elementow / 2)
q1 = x[43+1]
q2 = x [44+1]
print ("43cia cyfra w ciągu to : ", q1)
print ("44ta cyfra w ciągu to :", q2)
mediana = (q1 + q2) / 2
print ("mediana wynosi :", mediana)


        

