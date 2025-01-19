print('\n--- Oleh L200220037 ---')

def cari_indeks(daftar, target):
    indeks = []
    for i, elemen in enumerate(daftar):
        if elemen == target:
            indeks.append(i)
    return indeks

# Contoh penggunaan
daftar_mahasiswa = ["jamet", "wawa", "nadia","jamet", "wawa", "nadia","jamet", "wawa", "nadia",]
hasil_pencarian = cari_indeks(daftar_mahasiswa, "jamet")
print("Indeks lokasi mahasiswa 'jamet':", hasil_pencarian)
hasil_pencarian = cari_indeks(daftar_mahasiswa, "wawa")
print("Indeks lokasi mahasiswa 'wawa':", hasil_pencarian)
hasil_pencarian = cari_indeks(daftar_mahasiswa, "nadia")
print("Indeks lokasi mahasiswa 'nadia':", hasil_pencarian)
hasil_pencarian = cari_indeks(daftar_mahasiswa, "aku")
print("Indeks lokasi mahasiswa 'aku':", hasil_pencarian)
