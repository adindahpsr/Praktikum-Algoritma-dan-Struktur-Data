import re
pola = r'([\w\.-]+)@([\w\.-]+)'
e = re.findall(pola, pola)
print(e)	##==> sekarang bagaimanakah hasilnya?
# Atau kita cetak satu per satu:
for tup in e:
    print('user', tup[0], 'dengan host:', tup[1])