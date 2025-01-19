print('\n--- Oleh L200220037 ---')
def binSe(kumpulan, target):
    indeks = []
    # Menginisialisasi indeks awal, indeks akhir, dan status temuan
    i = 0
    j = len(kumpulan) - 1

    # Melakukan pencarian biner selama indeks awal tidak melebihi indeks akhir
    while i <= j:
        # Menghitung indeks tengah
        tengah = (i + j) // 2
        # Jika elemen di tengah adalah target, tambahkan indeksnya ke dalam list indeks
        if kumpulan[tengah] == target:
            indeks.append(tengah)
            # Cek ke kiri dari indeks tengah untuk mencari kemungkinan elemen yang sama
            kiri = tengah - 1
            while kiri >= 0 and kumpulan[kiri] == target:
                indeks.append(kiri)
                kiri -= 1
            # Cek ke kanan dari indeks tengah untuk mencari kemungkinan elemen yang sama
            kanan = tengah + 1
            while kanan < len(kumpulan) and kumpulan[kanan] == target:
                indeks.append(kanan)
                kanan += 1
            # Setelah menemukan semua kemungkinan indeks, keluar dari loop
            break
        # Jika target kurang dari elemen di tengah, cari di bagian kiri
        elif target < kumpulan[tengah]:
            j = tengah - 1
        # Jika target lebih besar dari elemen di tengah, cari di bagian kanan
        else:
            i = tengah + 1

    # Mengembalikan list indeks lokasi elemen yang ditemukan
    return indeks

# Contoh penggunaan
kumpulan = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
target = 6
hasil = binSe(kumpulan, target)
if hasil:
    print("Elemen", target, "ditemukan pada indeks:", hasil)
else:
    print("Elemen", target, "tidak ditemukan.")

