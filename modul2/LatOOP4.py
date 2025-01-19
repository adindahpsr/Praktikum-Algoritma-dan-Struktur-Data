from LatOOP3 import Manusia

class Mahasiswa(Manusia):
    def __init__(self, nama, NIM, kota, us):
        super().__init__(nama)
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = [] #tugas 4   
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s    
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM    
    def ambilUangSaku(self):
        return self.uangSaku    
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = 'kenyang'

        # tugas 2.a
    def ambilKotaTinggal(self):
        return self.kotaTinggal

        # tugas 2.b
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru

        # tugas 2.c
    def ambilUangSakul(self):
        return self.uangSaku
    def tambahUangSaku(self,tambahSaku):
        self.uangSaku += tambahSaku

        # tugas 4
    def ambilKuliah(self, nama_kuliah):
        self.listKuliah.append(nama_kuliah)
        # tugas 5
    def hapusKuliah(self, nama_kuliah):
        if nama_kuliah in self.listKuliah:
            self.listKuliah.remove(nama_kuliah)
        else:
            print("Error: Mata kuliah tidak ditemukan.")

# tugas 6
class SiswaSMA(Manusia):
    def __init__(self, nama, sma):
        super().__init__(nama)
        self.sma = sma
    def __str__(self):
        s = self.nama + ', bersekolah di ' + str(self.sma)
        return s    
    def ambilNama(self):
        return self.nama
    def ambilsma(self):
        return self.sma

        # tugas 3
#def inputMahasiswaBaru():
 #       nama = input("Masukkan nama mahasiswa: ")
  #      NIM = input("Masukkan NIM mahasiswa: ")
   #     kota = input("Masukkan kota tempat tinggal mahasiswa: ")
    #    uang_saku = int(input("Masukkan jumlah uang saku mahasiswa: "))
        
     #   return Mahasiswa(nama, NIM, kota, uang_saku)
#mahasiswaBaru = inputMahasiswaBaru()

        
#m1 = Mahasiswa("Jamil", 234, "Surakarta", 250000)
#m2 = Mahasiswa("Andi",365,"Magelang",275000)
#m3 = Mahasiswa("Sri", 676,"Yogyakarta",240000)
#m9 = Mahasiswa("Adinda", 36, "surabaya", 250000) #tugas 2
#m7 = Mahasiswa("Aulia", 37, "Tuban", 270000) #tugas 3
m234 = Mahasiswa("Hapsari", 38, "Jakarta", 300000) #tugas 4

# m1.ambilNama()
# m2.ambilNIM()
# m3.ucapkanSalam()
# m3.keadaan
# m3.makan("gado-gado")
# m3.keadaan
# print(m3)

# 2.6
# daftar = [m1, m2, m3]
# for i in daftar: print(i.NIM)
# for i in daftar: print(i)
# daftar[2].ambilNama()

# 2.a 
#print(m9.ambilKotaTinggal())

# 2.b 
#m9.perbaruiKotaTinggal("Sleman")
#print(m9.ambilKotaTinggal())

# 2.c 
#print(m7.ambilUangSaku())
#print(m7.tambahUangSaku(50000))
#print(m7.ambilUangSaku())

# 4
#m234.listKuliah()
#m234.ambilKuliah("Matematika Diskrit")
#m234.listKuliah()
#m234.ambilKuliah("Algoritma dan Struktur Data")
#m234.listKuliah()
#m234.hapusKuliah("Matematika Diskrit")

#5
#m234.listKuliah
