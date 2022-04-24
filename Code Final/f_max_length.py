import f_len
def max_length(array):
    # fungsi yang digunakan untuk mencari panjang maksimal dari suatu elemen

    # KAMUS LOKAL
    # kolom, baris, j, i, length_max = int
    # arr_length_max = array of int

    # ALGORITMA
    kolom = f_len.f_len(array[0])
    baris = f_len.f_len(array)
    arr_length_max = [0 for i in range(kolom)]

    for j in range(kolom):
        length_max = f_len.f_len(array[0][j])
        for i in range(1, baris):
            if (f_len.f_len(array[i][j]) > length_max):
                length_max = f_len.f_len(array[i][j])
        arr_length_max[j] = length_max

    return arr_length_max