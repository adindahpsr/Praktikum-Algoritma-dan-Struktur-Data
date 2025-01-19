from LatOOP4 import Mahasiswa 
class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Python is cool.")

m4 = MhsTIF("Badu", 334, "Sragen", 230000)
m4.katakanPy()
print(m4)
m4.keadaan
m4.makan("pecel")
m4.keadaan
m4.ucapkanSalam()
