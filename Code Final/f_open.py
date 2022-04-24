import f_split ; import f_slice
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
        baris = f_split.f_split(isi,"\n")
        data = f_slice.f_slice(baris)

    hasil = []

    for line in data :
        if line != "":
            parsed_line = f_split.f_split(line,";")
            hasil += [parsed_line]
    return hasil