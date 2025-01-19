def ucapkanSalam():
    print("Assalamu 'alaikum!")

def sapa(nama):
    ucapkanSalam() # Ini memanggil fungsi ucapkanSalam() di atas.
    print('Halo',nama)
    print('Selamat belajar!')

def kuadratkan(b):
    h = b*b
    return h

print(ucapkanSalam())
print(sapa('adinda'))
b = kuadratkan(5)
b
k = 9
print('Bilangannya',k, '.kalau dipangkatkan jadinya', kuadratkan(k))
