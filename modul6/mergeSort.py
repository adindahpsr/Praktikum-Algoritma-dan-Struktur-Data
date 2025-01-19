def mergeSort(A):
    #print("Membelah	", A)
    if len(A) > 1:
        mid = len(A) // 2	# Membelah list.
        separuhKiri = A[:mid]	# Slicing ini langkah yang expensive sebenarnya,
        separuhKanan = A[mid:]  #	bisakah kamu membuatnya lebih baik?
        
        mergeSort(separuhKiri)  # Ini rekursi. Memanggil lebih lanjut mergeSort
        mergeSort(separuhKanan)  #	untuk separuhKiri dan separuhKanan.
        #Di bawah ini adalah proses penggabungan.
        i=0  ;  j=0  ;  k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:  # while-loop ini
                A[k] = separuhKiri[i]	#	menggabungkan kedua list, yakni
                i = i + 1	#	separuhKiri dan separuhKanan,
            else:	#	sampai salah satu kosong.
                A[k] = separuhKanan[j]	# Perhatikan kesamaan strukturnya
                j = j + 1	#	dengan proses penggabungan
            k=k+1
        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1 
            k = k + 1 
        while j < len(separuhKanan):  # Jika separuhKanan mempunyai sisa
            A[k] = separuhKanan[j]	#	tumpukkan ke A
            j = j + 1	#	satu demi satu.
            k = k + 1 
            
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist) 
print(alist)