#Palindrom
#Kajak
#Elf układał kufle
#A to kanapa pana Kota

#slowo = input("Wpisz slowo: ")

# 3 formy range-a":
#range(100) #[0, 100) domknięcie miękkie czyli nie osiaga wartości 100
#range(90, 100) #[90, 100)
#range(90, 100, 2) #[90, 92, 94, 96, 98]

#slowo=input(("Wprowadz słowo: "))
#if(slowo==slowo[::-1]):
      #print("Słowo jest palindromem")
#else:
      #print("Słowo nie jest palindromem")



str = input("Wprowadź słowo: ")
l = len(str)
p = l-1
i = 0
while i < p:
    if str[i] != str[p-1]:
        print("Słowo jest palindromem")
        break
    else:
        print("Słowo nie jest palindromem")
        break