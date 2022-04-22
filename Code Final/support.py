# Fungsi baca csv
def f_open (path):
    with open(path) as f:
        isi = f.read()
        baris = f_split(isi,"\n")

        # header = baris[0].split(";")
        data = f_slice(baris)

    hasil = []

    for line in data :
        if line != "":
            parsed_line = f_split(line,";")
            hasil += [parsed_line]
    return hasil

# append
def f_append (array, string):
    list = ['*' for i in range(f_len(array)+1)]
    for i in range (f_len(array)+1):
        if i < f_len(array):
            list[i] = array[i]
        else:
            list[i] = string
    return list

# len
def f_len(array):
    count = 0
    for i in array:
        count += 1
    
    return count

# split
def f_split(value, delimiter):
    result = []
    string = ""
    for char in value:
        if char not in (delimiter):
            string += char
        else:
            result = f_append(result, string)
            string = ""
    result = f_append(result,string)
    return result

# slice
def f_slice (array):
    data = []
    for i in range(1, f_len(array)):
        data += [array[i]]
    return data

# join
def f_join(value, delimiter):
    result = ""

    for i in range(f_len(value)):
        result += str(value[i])

        if i != (f_len(value) - 1) :
            result += delimiter
    
    return result

# ini cara untuk balikin data yg udah di parsed ke bentuk awal waktu baca file csv (variabel isi di fungsi f_open)
'''
to_write = f_join(header, ";") + "\n"
for line in hasil:
    to_write += f_join(line, ";") + "\n"
'''

# search
def f_search(array, search):
    found = False
    for i in range(f_len(array)):
        if array[i] == search:
            found = True
    
    if found == True:
        return True
    else:
        return False

# mencari karakter paling panjang
def max_length(array):
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
    