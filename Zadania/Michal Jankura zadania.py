n = int(input("Zadaj n : "))

#úloha číslo 1
for i in range(n):
    print((i+1)*"*")
#úloha číslo 2
for i in range(n):
    print((n-i)*" " + n*"*")

#úloha číslo 3
for i in range(n+1):
    print(n*" "+i*"*")
    n -= 1
