print('\n--- Oleh L200220037 ---') 

import re 
a = open('Indonesia.txt','r') 
baca = a.read() 
a.close 
cocok= re.findall(r"di\w+",baca) 
print(cocok) 