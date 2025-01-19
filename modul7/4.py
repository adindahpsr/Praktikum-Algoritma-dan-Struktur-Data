print('\n--- Oleh L200220037 ---')

import re 
f = open('KEI.html', 'r', encoding='latin1') 
teks = f.read() 
f.close() 
i = r'\s<td>[\d.\w/]+</td>' 
p = r'(\w+)</a></td>' + i + i + i + r'\s<td>([\d.\w/]+)</td>' 
cocok = re.findall(p, teks) 
cocok1 = [(i[0], float(i[1])) for i in cocok] 
print(cocok1)