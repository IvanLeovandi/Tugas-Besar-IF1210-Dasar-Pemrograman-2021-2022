def f_len(array):
    # fungsi yang digunakan untuk mencari panjang dari sebuah array

    # KAMUS LOKAL
    # count, i = int

    # ALGORITMA
    count = 0
    for i in array:
        count += 1
    
    return count

def f_append (array, string):
    # fungsi yang digunakan untuk menambahkan elemen pada array

    # KAMUS LOKAL
    # list = array of char
    # i = int
    
    # ALGORITMA
    list = ['*' for i in range(f_len(array)+1)]
    for i in range (f_len(array)+1): # menambahkan 1 ruang untuk diisi elemen baru
        if i < f_len(array):
            list[i] = array[i]
        else: # ketika i = f_len(array) + 1, masukan elemen baru pada array
            list[i] = string
    return list

def f_search(array, search):
    # fungsi yang digunakan untuk mencari suatu elemen pada suatu array

    # KAMUS LOKAL
    # found = bool
    # i = count
    
    # ALGORITMA
    found = False
    for i in range(f_len(array)):
        if array[i] == search:
            found = True
    
    if found == True:
        return True
    else:
        return False

def f_split(value, delimiter):
    # fungsi yang digunakan untuk memisahkan data berdasarkan delimiter yang dimasukkan

    # KAMUS LOKAL
    # result = array of value
    # string = str
    # char = char

    # ALGORITMA
    result = []
    string = ""
    for char in value:
        if not f_search(delimiter,char): # jika karakter pada value bukan merupakan delimiter
            string += char # maka char akan ditambahkan pada variabel string
        else:
            result = f_append(result, string) # jika ditemukan delimiter, maka string akan dimasukkan pada array result
            string = "" # mengubah variabel string menjadi string kosong
    result = f_append(result,string)
    return result

def f_slice (array):
    # fungsi yang digunakan untuk mengambil data dari indeks ke 1 sampai akhir (untuk menghilangkan header pada variabel data)

    # KAMUS LOKAL
    # data = array of array
    # i = int

    # ALGORITMA
    data = []
    for i in range(1, f_len(array)):
        data += [array[i]]
    return data

def f_open (path):
    # fungsi yang digunakan untuk membaca file dan menyimpan datanya dalam array of array

    # KAMUS LOKAL
    # isi,line = string
    # parsed_line = array of string
    # baris, data = array of isi
    # hasil = array of parsed_line
    
    # ALGORITMA
    with open(path) as f:
        isi = f.read()
        baris = f_split(isi,"\n")
        data = f_slice(baris)

    hasil = []

    for line in data :
        if line != "":
            parsed_line = f_split(line,";")
            hasil += [parsed_line]
    return hasil

def max_length(array):
    # fungsi yang digunakan untuk mencari panjang maksimal dari suatu elemen

    # KAMUS LOKAL
    # kolom, baris, j, i, length_max = int
    # arr_length_max = array of int

    # ALGORITMA
    kolom = f_len(array[0])
    baris = f_len(array)
    arr_length_max = [0 for i in range(kolom)]

    for j in range(kolom):
        length_max = f_len(array[0][j])
        for i in range(1, baris):
            if (f_len(array[i][j]) > length_max):
                length_max = f_len(array[i][j])
        arr_length_max[j] = length_max

    return arr_length_max
    
