##Nomer 8
import timeit
import matplotlib.pyplot as plt

print("Nomer 8")
def soal_tujuh(n):
    L = list(range(30))
    L = L[::-1]
    for i in range(n):
        for b in range(n):
            L.insert(i,b)

def uji_soal_tujuh(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = "from __main__ import soal_tujuh"
    for i in jangkauan:
        ##print('i = ',i)
        t = timeit.timeit("soal_tujuh(" + str(i) + ")", setup=siap, number=1)
        ls.append(t)
    return ls

n = 10
LS = uji_soal_tujuh(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()
