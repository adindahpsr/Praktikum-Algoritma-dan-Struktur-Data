mdef gabungkanDuaListUrut(A, B):
    la = len(A); lb = len(B)
    C = list()	# C adalah list baru 
    i = 0; j = 0 
    
    # Gabungkan keduanya sampai salah satu kosong 
    while i < la and j < lb:
        if A[i] < B[j]:
            C.append(A[i]) 
            i += 1
        else:
            C.append(B[j]) 
            j += 1
    
    while i < la:
        C.append(A[i]) 
        i += 1
        
    while j < lb:
        C.append(B[j]) 
        j += 1
    return C