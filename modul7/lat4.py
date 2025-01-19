import re
pola  =  r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
cocok = re.findall(r'[\w.-]+@[\w.-]+', pola)
print(cocok[0])	## => ’dita-b@google.com’
