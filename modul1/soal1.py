def cetakSiku(x):
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            print('*', end=" ")
        print()
        
print('\n--- Oleh L200220037 ---')
        
# meminta input tinggi segitiga dari pengguna
tinggi_segitiga = int(input("Masukkan tinggi segitiga(bilangan bulat)"))

# memanggil fungsi cetak_segitiga dengan input tinggi segitiga
cetakSiku(tinggi_segitiga)
