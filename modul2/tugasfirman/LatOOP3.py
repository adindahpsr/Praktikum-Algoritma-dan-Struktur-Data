class Manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = "kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self,n):
        return n*2

p1 = Manusia("Fatimah")
p1.ucapkanSalam()

# p2 = Manusia("Budi")
# p2.ucapkanSalam()
# ak = Manusia("Abdul karim")
# ak.ucapkanSalam()
# ak.keadaan
# ak.olahraga("renang")
# ak.keadaan
# ak.makan("bakso")
# ak.keadaan
# ak.mengalikanDenganDua(8)