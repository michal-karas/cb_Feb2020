def fibbonaci_numbers(n):
    ''' zwraca liczby Fibonacciego mniejsze od n '''
    wynik = []
    a, b = 0, 1
    while a < n:
        wynik.append(a)
        a, b = b, a+b
    return wynik

x = fibbonaci_numbers(100)
print(x)
print(fibbonaci_numbers.__doc__)