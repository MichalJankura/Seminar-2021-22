meno = input("zadaj meno :")
c = len(meno)
#do riadku
for q in range(c):
    print(meno,end=" ")
#pod seba
for i in range(c):
    print(f"{meno}")

c = c+6
print(c*"*")
print(f"*  {meno}  *")
print(c*"*")

print(meno[::-1])

for i in range(len(meno)):
    print(meno[i]*(i+1))
