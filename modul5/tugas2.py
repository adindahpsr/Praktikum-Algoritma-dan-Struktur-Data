print('\n--- Oleh L200220037 ---')
#menggabungkan a dan b menjadi c

A = [1,4,5,6,9] 
B = [2,3,7,8,10] 
def gabungan(x,y): 
    a = len(A) 
    b = len(B) 
    c = list() 
    d,e = 0,0 
    while d < a and e < b: 
        if x[d] < y[e]: 
            c.append(x[d]) 
            d +=1 
        else: 
            c.append(y[e]) 
            e +=1 
    while d < a: 
        c.append(x[d]) 
        d +=1 
    while e < b: 
        c.append(y[e]) 
        e +=1 
    return c 

C = gabungan(A,B) 
print(C)