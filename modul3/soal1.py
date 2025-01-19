print('\n--- Oleh L200220037 ---')

class Matrix:
    #point 1
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        self.validasi()

    def validasi(self):
        for baris in self.data:
            if len(baris) != self.cols:
                raise ValueError("Matriks memiliki panjang baris yang tidak konsisten.")
            for elemen in baris:
                if not isinstance(elemen, (int, float)):
                    raise ValueError("Elemen-elemen matriks harus berupa bilangan bulat atau pecahan.")
#point 2
    def ukuran(self):
        return self.rows, self.cols
#point 3
    def penjumlahan(self, lainnya):
        if self.ukuran() != lainnya.ukuran():
            raise ValueError("Matriks harus memiliki ukuran yang sama.")
        hasil = []
        for i in range(self.rows):
            hasil.append([self.data[i][j] + lainnya.data[i][j] for j in range(self.cols)])
        return Matrix(hasil)
#point 4
    def perkalian(self, lainnya):
        if self.cols != lainnya.rows:
            raise ValueError("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
        hasil = []
        for i in range(self.rows):
            baris_hasil = []
            for j in range(lainnya.cols):
                elemen_hasil = sum(self.data[i][k] * lainnya.data[k][j] for k in range(self.cols))
                baris_hasil.append(elemen_hasil)
            hasil.append(baris_hasil)
        return Matrix(hasil)
#point 5
    def hitungDeterminan(self):
        if self.rows != self.cols:
            raise ValueError("Determinan hanya dapat dihitung untuk matriks persegi.")
        if self.rows == 1:
            return self.data[0][0]
        elif self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        else:
            det = 0
            for i in range(self.rows):
                det += (-1) ** i * self.data[0][i] * self.submatriks(0, i).hitungDeterminan()
            return det

    def submatriks(self, baris, kolom):
        return Matrix([baris[:kolom] + baris[kolom + 1:] for baris in (self.data[:baris] + self.data[baris + 1:])])


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix 1:")
print(matrix1.data)
print("Matrix 2:")
print(matrix2.data)

print("Ukuran Matrix 1:", matrix1.ukuran())
print("Ukuran Matrix 2:", matrix2.ukuran())

print("Penjumlahan Matrix:")
print(matrix1.penjumlahan(matrix2).data)

print("Perkalian Matrix:")
print(matrix1.perkalian(matrix2).data)

print("Determinan Matrix 1:", matrix1.hitungDeterminan())

