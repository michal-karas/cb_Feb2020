print("podaj liczbę dla której obliczymy kod fibonacciego")
x=input()
x0=0
x1=1
if x == 0:
    print(0)
elif x == 1:
    print(1)
else: 
     for element in range(2,20):
      x0=x1
      x1=x2
      x2=x1+x0
print(x2)