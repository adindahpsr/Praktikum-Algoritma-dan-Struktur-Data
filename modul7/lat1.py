import re
s = 'sebuah contoh kata:teh!!'
t = 'sebuah contoh kata:batagor!!'
r = 'sebuah contoh kata:es teh!!'
cocok = re.findall(r'kata:\w\w\w', r)

# Pernyataan-IF sesudah findall() akan memeriksa apakah pencarian berhasil:
if cocok:
    print('menemukan', cocok ) ## ’menemukan [kata:teh]’
else:
    print('tidak  menemukan')