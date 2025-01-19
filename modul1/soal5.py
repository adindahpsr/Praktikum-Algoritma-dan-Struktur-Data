from math import sqrt as sq
def apakahPrima(n):
    n = int(n) #kalau pecahan, dibuang pecahannya
    assert n>=0 #hanya menerima bilangan non-negatif
    primaKecil = [2,3,5,7,9,11] #kalau angkanya kecil, akan
    bukanPrKecil = [0,1,4,6,8,9,10] #tertangkap disini
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1): #cukup smp akarnya
            if n%i==0: #tugas
                return False #tugas
            return True #tugas
        
print('\n--- Oleh L200220037---')

print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))