def formatRupiah(BilanganBulatPositif): 
    Hasil = "" 
    x = 0 
    for i in str(BilanganBulatPositif) [::-1]: 
        if x < 3: 
            Hasil += i 
            x += 1 
        else: 
                Hasil = Hasil + "." + i 
                x = 1 
    return "Rp. " + Hasil[::-1] 
 
print('\n--- Oleh L200220037---')

print(formatRupiah(15000))
print(formatRupiah(5372000))
print(formatRupiah(13000))
print(formatRupiah(10870))