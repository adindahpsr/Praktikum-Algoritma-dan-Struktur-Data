##Nomer 9
import timeit
import time

print("Nomer 9")
def carilurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False
def tim():
    z=100
    a = [8, 7, 2, 1, 3, 2, 10]
    awal = time.time()
    U = carilurus(a, z)
    akhir=time.time()
    print("==========================worst case ")
    print("mengurutkan %d bilangan, memerlukan %8.7f detik" %(U,akhir-awal))
tim()

import matplotlib.pyplot as plt
def tim_matlib(n):
    z=100
    a = [8, 7, 2, 1, 3, 2, 10]
    U = carilurus(a, n)

def uji_soal_sembilan(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = "from __main__ import tim_matlib"
    for i in jangkauan:
        t = timeit.timeit("tim_matlib(" + str(i) + ")", setup=siap, number=1)
        ls.append(t)
    return ls

n = 10
LS = uji_soal_sembilan(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()
