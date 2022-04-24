import f_search ; import f_append
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
        if not f_search.f_search(delimiter,char): # jika karakter pada value bukan merupakan delimiter
            string += char # maka char akan ditambahkan pada variabel string
        else:
            result = f_append.f_append(result, string) # jika ditemukan delimiter, maka string akan dimasukkan pada array result
            string = "" # mengubah variabel string menjadi string kosong
    result = f_append.f_append(result,string)
    return result