print('\n--- Oleh L200220037 ---')

class Matrix:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    @classmethod
    def buatNol(cls, m, n=None):
        if n is None:
            n = m
        return cls([[0] * n for _ in range(m)])

    @classmethod
    def buatIdentitas(cls, m):
        return cls([[1 if i == j else 0 for j in range(m)] for i in range(m)])


# Contoh Penggunaan
matriks_nol_3x3 = Matrix.buatNol(3, 3)
matriks_nol_4x4 = Matrix.buatNol(4)
matriks_identitas_3x3 = Matrix.buatIdentitas(3)

print("Matriks Nol 3x3:")
print(matriks_nol_3x3.data)

print("\nMatriks Nol 4x4:")
print(matriks_nol_4x4.data)

print("\nMatriks Identitas 3x3:")
print(matriks_identitas_3x3.data)
