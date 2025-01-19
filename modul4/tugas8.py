print('\n--- Oleh L200220037 ---')

a=58
b=1
print("Permainan tebak angka.")
print("Saya menyimpan sebuah bilangan bulat antara 1 sampai 100. Coba tebak.")
while True:
    i = int(input(f"Masukkan tebakkan ke-{b}:>"))
    if i < a:
        print("Itu terlalu kecil. Coba lagi.")
    elif i > a:
        print("Itu terlalu besar. Coba lagi.")
    elif i == a:
        print("Ya. Anda benar")
        break
    b+=1