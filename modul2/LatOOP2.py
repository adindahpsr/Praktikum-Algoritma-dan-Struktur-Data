class Pesan(object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("Kalimatku mempunyai",len(self.teks),"karakter.")
    def perbarui(self,stringBaru):
        self.teks = stringBaru
        
         # tugas 1.a
    def apakahTerkandung(self, string):
        return string in self.teks
        # tugas 1.b
    def hitungKonsonan(self):
        konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        jumlah_konsonan = 0
        for karakter in self.teks:
            if karakter in konsonan:
                jumlah_konsonan += 1
        return jumlah_konsonan
        # tugas 1.c 
    def hitungVokal(self):
        Vokal = "aiueoAIUEO"
        jumlah_Vokal = 0
        for karakter in self.teks:
            if karakter in Vokal:
                jumlah_Vokal += 1
        return jumlah_Vokal
        
        
# pesanA = Pesan("Aku suka kuliah ini")
# pesanB = Pesan("Surakarta: the Spirit of Java")
# pesanA.cetakIni()
# pesanA.cetakJumlahKarakterku()
# pesanB.cetakJumlahKarakterku()
# pesanA.cetakPakaiHurufKapital()
# pesanA.cetakPakaiHurufKecil()
# pesanA.perbarui("Aku senang struktur data")
# pesanA.cetakIni()

# tugas 1
p9 = Pesan("Indonesia adalah negeri yang indah")
print(p9.apakahTerkandung("ege"))
print(p9.apakahTerkandung("eka"))

p10 = Pesan("Surakarta")
print(p10.hitungKonsonan())

print(p10.hitungVokal())