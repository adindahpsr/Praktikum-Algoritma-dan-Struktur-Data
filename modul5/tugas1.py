print('\n--- Oleh L200220037 ---')

class MhsTIF(object): 
    def __init__(self,nama,nim,kota,us): 
        self.nama = nama 
        self.NIM = nim 
        self.kota = kota 
        self.uangSaku = us
    # Fungsi untuk mengurutkan array mahasiswa berdasarkan NIM
    def urutkan_mahasiswa(daftar):
        daftar.sort(key=lambda x: x.NIM)  # Mengurutkan daftar berdasarkan NIM
        return daftar
        
m0 = MhsTIF('Adinda Aulia Hapsari',10,'Karanganyar', 240000) 
m1 = MhsTIF('Dian Sasya Fitriani',51,'Sragen', 230000)
m2 = MhsTIF('Nasyawa Adesty Riyanni',2,'Surakarta', 250000)
m3 = MhsTIF('Nadia Maharani Zulvika',18,'Surakarta', 235000) 
m4 = MhsTIF('Naufal Adiza',4,'Surabaya', 240000)
m5 = MhsTIF('Istiqomah Zulfa Nuraini',31,'Salatiga', 250000) 
m6 = MhsTIF('Nadiya Almastuti',13,'Klaten', 245000)
m7 = MhsTIF('Nur Maulana Fathurrahman',5,'Wonogiri', 245000) 
m8 = MhsTIF('Adam Pinggala Aruna',23,'Klaten', 245000)
m9 = MhsTIF('Zidane Arrazzak Azmi',64,'Karanganyar', 270000) 
m10 = MhsTIF('Dilla Maya',29,'Purwodadi', 265000)         
Daftar = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]

# Panggil fungsi untuk mengurutkan daftar mahasiswa berdasarkan NIM
Daftar = MhsTIF.urutkan_mahasiswa(Daftar)

# Cetak daftar mahasiswa yang sudah diurutkan
print("Daftar Mahasiswa TIF yang sudah diurutkan berdasarkan NIM:")
for mhs in Daftar:
    print("\nNama:", mhs.nama, "\nNIM:", mhs.NIM, "\nAlamat:", mhs.kota, "\nUang Saku:", mhs.uangSaku)