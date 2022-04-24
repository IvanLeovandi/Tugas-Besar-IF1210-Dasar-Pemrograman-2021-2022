import f_len
def f_search(array, search):
    # fungsi yang digunakan untuk mencari suatu elemen pada suatu array

    # KAMUS LOKAL
    # found = bool
    # i = count
    
    # ALGORITMA
    found = False
    for i in range(f_len.f_len(array)):
        if array[i] == search:
            found = True
    
    if found == True:
        return True
    else:
        return False