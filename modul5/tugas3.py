print('\n--- Oleh L200220037 ---')

def swap(A,p,q): 
    tmp = A[p] 
    A[p] = A[q] 
    A[q] = tmp 

def cariPosisiYangTerkecil(A,dariSini,sampaiSini): 
    posisiYangTerkecil = dariSini 
    for i in range(dariSini+1, sampaiSini): 
        if A[i] < A[posisiYangTerkecil]: 
            posisiYangTerkecil = i 
        return posisiYangTerkecil 

def bubbleSort(A): 
    n = len(A) 
    for i in range(n-1): 
        for j in range(n-i-1): 
            if A [j] > A[j+i]: 
                swap(A,j,j+i) 

def selectionSort(A): 
    n = len(A) 
    for i in range(n-1): 
        indexKecil = cariPosisiYangTerkecil(A,i,n) 
        if indexKecil !=i : 
            swap(A,i,indexKecil) 

def insertionSort(A): 
    n = len(A) 
    for i in range(1,n): 
        nilai = A[i] 
        pos = i 
        while pos > 0 and nilai < A[pos - 1]: 
            A[pos] = A[pos - 1] 
            pos = pos -1 
        A[pos] = nilai 

from time import time as detak 
from random import shuffle as kocok 
k = [i for i in range(1,6001)] 
kocok(k) 
u_bub = k[:] 
u_sel = k[:] 
u_ins = k[:] 

aw = detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw)); 
aw = detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw)); 
aw = detak();insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw));