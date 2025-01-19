def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1 )
    
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)	# Atur elemen dan dapatkan titikBelah.
        quickSortBantu(A, awal, titikBelah - 1)  # Ini rekursi untuk belah sisi kiri
        quickSortBantu(A, titikBelah + 1, akhir)
        
def partisi(A, awal, akhir):
    nilaiPivot = A[awal] # Di sini nilaiPivot kita ambil dari elemen yang paling kiri.
    
    penandaKiri = awal + 1 # Posisi awal penandaKiri. Lihat Gambar 6.3.
    penandaKanan = akhir	# Posisi awal penandaKanan.
    
    selesai = False
    while not selesai: # loop di bawah adalah untuk mengatur ulang posisi semua elemen
        while penandaKiri <= penandaKanan and \	# penandaKiri bergerak ke kanan,
            A[penandaKiri] <= nilaiPivot:	#  sampai ketemu suatu nilai yang
            penandaKiri = penandaKiri + 1	#  lebih besar dari nilaiPivot
        while A[penandaKanan] >= nilaiPivot and \ # penandaKanan bergerak ke kiri,
            penandaKanan >= penandaKiri:	#  sampai ketemu suatu nilai yang
            penandaKanan = penandaKanan - 1	#  lebih kecil dari nilaiPivot
        if penandaKanan < penandaKiri:	# Kalau dua penanda sudah bersilangan,
            selesai = True	#  selesai & lanjut ke penempatan pivot
        else:
            temp = A[penandaKiri]	# Tapi kalau belum bersilangan,
            A[penandaKiri] = A[penandaKanan]	#  tukarlah isi yang ditunjuk oleh
            A[penandaKanan] = temp	#  penandaKiri dan penandaKanan
    temp = A[awal]	# Kalau acara tukar menukar posisi sudah selesai,
    A[awal] = A[penandaKanan]	#  kita lalu menempatkan pivot pada posisi yang tepat,
    A[penandaKanan] = temp	#  yakni posisi penandaKanan. Lihat Gambar 6.3 dan 6.4. 
    #  Posisi penandaKanan adalah juga titikBelah.
    
    return penandaKanan	