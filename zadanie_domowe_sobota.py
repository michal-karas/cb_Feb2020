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

worst_score = 100
worst_score = data[0]["score"]
for entry in data:
    if entry["score"] <= worst_score:
        worst_score = entry["score"]
        worst_title = entry["title"]

print(f"Najgorsza ocena filmu RdN to: {worst_score}")
print(f"Tytuł najgorszego filmu to {worst_title}")


best_score = 100
best_score = data[0]["score"]
for entry in data:
    if entry["score"] > best_score:
        best_score = entry["score"]
        best_title = entry["title"]

print(f"Najlepsza ocena filmu RdN to: {best_score}")
print(f"Tytuł najlepszego filmu to {best_title}")


suma = 0
list_of_elements = 0
for entry in data:
    suma += entry["score"]
    list_of_elements += 1

print("Średnia ocen z wszytskich filmów Roberta to: ", suma / list_of_elements)

