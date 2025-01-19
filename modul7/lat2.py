import re
# Dua baris ini mencari pola ’eee’ di string ’teeeh’.
# Seluruh pola harus cocok, tapi itu bisa muncul di mana saja.
# Jika berhasil, \texttt{cocok} adalah daftar semua teks yang cocok.

def cocok(a):
    if cocok:
        print('menemukan', cocok ) ## ’menemukan [kata:teh]’
    else:
        print('tidak  menemukan')
        
cocok1 = re.findall(r'eee', 'teeeh') 
cocok(cocok1)

cocok2 = re.findall(r'ehs', 'teeeh') 
cocok(cocok2)

# . = semua karakter kecuali \n
cocok3 = re.findall(r'..h', 'teeeh') 
cocok(cocok3)

# \d = karakter angka, \w = karakter huruf atau angka
cocok4 = re.findall(r'\d\d\d', 't123h di 2019 bulan 02') 
cocok(cocok4)

cocok5 = re.findall(r'\w\w\w', '@@a*bc#def*tghh!!') 
cocok(cocok5)