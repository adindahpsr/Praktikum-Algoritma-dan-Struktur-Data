print('\n--- Oleh L200220037 ---')

#nomer6

class simpulpohonbiner(object):
    def __init__ (self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

def ukuranpohon (akar, count = 0 ):
    if akar is None :
        return count

    return ukuranpohon(akar.kiri, ukuranpohon(akar.kanan, count +1))

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
