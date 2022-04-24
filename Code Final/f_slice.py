import f_len
def f_slice (array):
    # fungsi yang digunakan untuk mengambil data dari indeks ke 1 sampai akhir (untuk menghilangkan header pada variabel data)

    # KAMUS LOKAL
    # data = array of array
    # i = int

    # ALGORITMA
    data = []
    for i in range(1, f_len.f_len(array)):
        data += [array[i]]
    return data