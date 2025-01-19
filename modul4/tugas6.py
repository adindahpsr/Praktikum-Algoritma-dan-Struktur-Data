print('\n--- Oleh L200220037 ---')

def binSe(kumpulan, target):
    # Menginisialisasi indeks awal, indeks akhir, dan status temuan
    i = 0
    j = len(kumpulan) - 1
    found = False

    # Melakukan pencarian biner selama indeks awal tidak melebihi indeks akhir dan elemen belum ditemukan
    while i <= j and not found:
        # Menghitung indeks tengah
        tengah = (i + j) // 2
        # Jika elemen di tengah adalah target, set status temuan menjadi True
        if kumpulan[tengah] == target:
            found = True
        # Jika target kurang dari elemen di tengah, cari di bagian kiri
        elif target < kumpulan[tengah]:
            j = tengah - 1
        # Jika target lebih besar dari elemen di tengah, cari di bagian kanan
        else:
            i = tengah + 1

    # Jika elemen ditemukan, kembalikan indeksnya
    if found:
        return tengah
    # Jika elemen tidak ditemukan, kembalikan False
    else:
        return False

# Contoh penggunaan
kumpulan = [2, 3, 5, 7, 11, 13, 17, 19, 23]
target = 11
hasil = binSe(kumpulan, target)
if hasil is not False:
    print("Elemen", target, "ditemukan pada indeks:", hasil)
else:
    print("Elemen", target, "tidak ditemukan.")
