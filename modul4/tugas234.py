print('\n--- Oleh L200220037 ---')

class MhsTIF:
    def __init__(self, nama, nim, alamat, us):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
        self.us = us

#no2
def uangSaku_terkecil(daftar):
    # Menginisialisasi nilai uang saku terkecil dengan uang saku mahasiswa pertama dalam daftar
    uangSaku_min = daftar[0].us
    # Melakukan iterasi untuk mencari uang saku terkecil
    for mhs in daftar:
        if mhs.us < uangSaku_min:
            uangSaku_min = mhs.us
    return uangSaku_min

#no3
def mahasiswa_uang_saku_terkecil(daftar):
    # Menginisialisasi nilai uang saku terkecil dengan uang saku mahasiswa pertama dalam daftar
    uangSaku_min = daftar[0].us
    # Melakukan iterasi untuk mencari nilai uang saku terkecil
    for mhs in daftar:
        if mhs.us < uangSaku_min:
            uangSaku_min = mhs.us
    # Membuat list untuk menyimpan semua objek mahasiswa yang memiliki uang saku terkecil
    mahasiswa_terkecil = []
    # Melakukan iterasi lagi untuk mencari semua mahasiswa dengan uang saku terkecil
    for mhs in daftar:
        if mhs.us == uangSaku_min:
            mahasiswa_terkecil.append(mhs)
    return mahasiswa_terkecil

#no4
def usKurang(daftar, batas):
    mahasiswa_kurang_dari = []
    for mhs in daftar:
        if mhs.us < batas:
            mahasiswa_kurang_dari.append(mhs)
    return mahasiswa_kurang_dari

c0 = MhsTIF('Adinda Aulia',10,'Sukoharjo', 240000) 
c1 = MhsTIF('Dian Sasya',51,'Sragen', 230000)
c2 = MhsTIF('Memet',2,'Surakarta', 250000)
c3 = MhsTIF('Arya Veda',18,'Surakarta', 235000) 
c4 = MhsTIF('Ganza',4,'Boyolali', 240000)
c5 = MhsTIF('Damar Galih',31,'Salatiga', 250000) 
c6 = MhsTIF('Izzat',13,'Klaten', 245000)
c7 = MhsTIF('Adz Dzaka',5,'Wonogiri', 245000) 
c8 = MhsTIF('Ahmad Taslim',23,'Klaten', 245000)
c9 = MhsTIF('Yanto',64,'Karanganyar', 270000) 
c10 = MhsTIF('Sugeng',29,'Purwodadi', 265000) 
## Lalu kita membuat daftar mahasiswa dalam bentuk list seperti ini: 
Daftar = [c0, c1, c2, c3, c4, c5, c6, c7,c8, c9,c10]

#lat
target = 'Surakarta' 
for i in Daftar:
    if i.alamat == target:
        print(i.nama + ' tinggal di ' + target)
        
#panggil no2
uangSaku_min = uangSaku_terkecil(Daftar)
print("Uang saku terkecil:", uangSaku_min)

#panggil no3
mahasiswa_terkecil = mahasiswa_uang_saku_terkecil(Daftar)
print("Mahasiswa dengan uang saku terkecil:")
for mhs in mahasiswa_terkecil:
    print("Nama:", mhs.nama, "\nUang Saku:", mhs.us)
    
#panggil no4
batas = 250000
mahasiswa_kurang_dari = usKurang(Daftar, batas)

# Mencetak informasi mahasiswa yang uang sakunya kurang dari 250.000
print("Mahasiswa dengan uang saku kurang dari", batas, ":")
for mhs in mahasiswa_kurang_dari:
    print("Nama:", mhs.nama, "\nUang Saku:", mhs.us)