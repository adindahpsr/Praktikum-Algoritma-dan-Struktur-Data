print('\n--- Oleh L200220037 ---')

#nomer8

class simpulpohonbiner(object):
    def __init__ (self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

def cetak(subpohon, count = 0):
    if subpohon is not None:
        print (subpohon.data + ',level ' + str (count))
        (cetak(subpohon.kiri, count + 1), cetak(subpohon.kanan, count + 1))

a = simpulpohonbiner ('Ambarawa')
b = simpulpohonbiner ('Bantul')
c = simpulpohonbiner ('Cimahi')
d = simpulpohonbiner ('Denpasar')
e = simpulpohonbiner ('Enrekang')
f = simpulpohonbiner ('Flores')
g = simpulpohonbiner ('Garut')
h = simpulpohonbiner ('Halmahera Timur')
i = simpulpohonbiner ('Indramayu')
j = simpulpohonbiner ('Jakarta')

a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kiri = f; c.kanan = g
e.kiri = h
g.kanan = i
