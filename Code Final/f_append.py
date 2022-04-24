import f_len
def f_append (array, string):
    # fungsi yang digunakan untuk menambahkan elemen pada array

    # KAMUS LOKAL
    # list = array of char
    # i = int
    
    # ALGORITMA
    list = ['*' for i in range(f_len.f_len(array)+1)]
    for i in range (f_len.f_len(array)+1): # menambahkan 1 ruang untuk diisi elemen baru
        if i < f_len.f_len(array):
            list[i] = array[i]
        else: # ketika i = f_len(array) + 1, masukan elemen baru pada array
            list[i] = string
    return list