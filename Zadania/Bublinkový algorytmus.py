def bublinkovy(z):
    n = len(z)
    for i in range(n):
        for j in range(n-1):
            if z[j] > z [j + 1]:
                z[j],z[j + 1] = z[j + 1],z[j]
    return z
z = [5,9,3,2,19,11]
bublinkovy(z)
print(z)

def bublinkovy2(nz):
    z = list(nz)
    n = len(z)
    for j in range(n):
        for i in range(j,n):
            if z[i] < z[j]:
                z[i],z[j] = z[j],z[i]
