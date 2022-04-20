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
    
    if path == "user.csv":
        for line in hasil:
            line[5] = int(line[5])
    elif path == "game.csv":
        for line in hasil:
            line[4] = int(line[4])
            line[5] = int(line[5])
    elif path == "riwayat.csv":
        for line in hasil:
            line[2] = int(line[2])

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
#Kamus
#inventory : array of (array of string)
#game_valid : array of (array of string)
#game_id : string
#game_title : string
#game_price : string
#game_category : string
#game_year : string
#count = integer




#Algoritma
def search_game_at_store():
    inventory = f_open("game.csv")
    game_id = input("Masukkan ID Game: ")
    game_title = input("Masukkan Nama Game: ")
    game_price = input("Masukkan Harga Game: ")
    game_category = input("Masukkan kategori game: ")
    game_year = input("Masukkan Tahun Rilis Game: ")
    count = 0
    game_valid = ["*" for i in range (f_len(inventory))]


    if game_id == "":
        if game_title == "":
            if game_price == "":
                if game_category == "":
                    if game_year == "":
                        #Semua parameter kosong
                        for i in range(f_len(inventory)):
                            print(i+1, end=". ")
                            for j in range (f_len(inventory)):
                                print(inventory[i][j], end = " | ")
                            print()
                    else:
                        #Semua paramater kosong kecuali Tahun Rilis
                        for i in range (f_len(inventory)):
                            if inventory[i][3] == game_year:
                                game_valid[count] = inventory[i]
                                count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                else:
                    #Semua parameter kosong kecuali Kategori
                    if game_year == "":
                        for i in range(f_len(inventory)):
                            if inventory[i][2] == game_category:
                                game_valid[count] = inventory[i]
                                count += 1
                        print("Daftar game pada toko yang memenuhi kriteria: ")
                        for i in range(count):
                            print(i+1, end=". ")
                            for j in range (5):
                                print(game_valid[i][j], end=" | ")
                            print()
                    else:
                        #Parameter Tahun Rilis dan Kategori ada (tidak kosong)
                        for i in range (f_len(inventory)):
                            if inventory[i][2] == game_category:
                                if inventory[i][3] == game_year:
                                    game_valid[count] = inventory[i]
                                    count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
            else:
                if game_category == "":
                    if game_year == "":
                        #Semua parameter kosong kecuali Harga
                        for i in range(f_len(inventory)):
                            if int(game_price) == inventory[i][4]:
                                game_valid[count] = inventory[i]
                                count += 1
                        if not count == 0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                    else:
                        #Parameter Harga dan Tahun Rilis ada (tidak kosong)
                        for i in range (f_len(inventory)):
                            if inventory[i][4] == int(game_price):
                                if inventory[i][3] == game_year:
                                    game_valid[count] = inventory[i]
                                    count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                else:
                    if game_year == "":
                        #Parameter Harga dan Kategori ada (tidak kosong)
                        for i in range(f_len(inventory)):
                            if inventory[i][4] == int(game_price):
                                if inventory[i][2] == game_category:
                                    game_valid[count] = inventory[i]
                                    count += 1
                        print("Daftar game pada toko yang memenuhi kriteria: ")
                        for i in range(count):
                            print(i+1, end=". ")
                            for j in range (5):
                                print(game_valid[i][j], end=" | ")
                            print()
                    else:
                        for i in range (f_len(inventory)):
                            #Parameter Harga, Kategori dan Tahun Rilis ada (tidak kosong)
                            if inventory[i][4] == int(game_price):
                                if inventory[i][2] == game_category:
                                    if inventory[i][3] == game_year:
                                        game_valid[count] = inventory[i]
                                        count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
        else:
            if game_price == "":
                if game_category == "":
                    if game_year == "":
                        #Semua parameter kosong kecuali Nama
                        for i in range(f_len(inventory)):
                            if game_title == inventory[i][1]:
                                game_valid[count] = inventory[i]
                                count += 1
                        if not count == 0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                    else:
                        #Parameter Nama dan Tahun Rilis ada (tidak kosong)
                        for i in range (f_len(inventory)):
                            if game_title == inventory[i][1]:
                                if inventory[i][3] == game_year:
                                    game_valid[count] = inventory[i]
                                    count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                else:
                    if game_year == "":
                        #Parameter Nama dan Kategori ada (tidak kosong)
                        for i in range(f_len(inventory)):
                            if game_title == inventory[i][1]:
                                if inventory[i][2] == game_category:
                                    game_valid[count] = inventory[i]
                                    count += 1
                        print("Daftar game pada toko yang memenuhi kriteria: ")
                        for i in range(count):
                            print(i+1, end=". ")
                            for j in range (5):
                                print(game_valid[i][j], end=" | ")
                            print()
                    else:
                        #Parameter Nama, Kategori dan Tahun Rilis ada (tidak kosong)
                        for i in range (f_len(inventory)):
                            if game_title == inventory[i][1]:
                                if inventory[i][2] == game_category:
                                    if inventory[i][3] == game_year:
                                        game_valid[count] = inventory[i]
                                        count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
            else:
                if game_category == "":
                    if game_year == "":
                        #Parameter Nama dan Harga ada (tidak kosong)
                        for i in range(f_len(inventory)):
                            if game_title == inventory[i][1]:
                                if int(game_price) == inventory[i][4]:
                                    game_valid[count] = inventory[i]
                                    count += 1
                        if not count == 0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                    else:
                        for i in range (f_len(inventory)):
                            #Parameter Nama, Harga dan Tahun ada (tidak kosong)
                            if game_title == inventory[i][1]:
                                if inventory[i][4] == int(game_price):
                                    if inventory[i][3] == game_year:
                                        game_valid[count] = inventory[i]
                                        count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                else:
                    if game_year == "":
                        for i in range(f_len(inventory)):
                            #Parameter Nama, Harga dan Kategori ada (tidak kosong)
                            if game_title == inventory[i][1]:
                                if inventory[i][4] == int(game_price):
                                    if inventory[i][2] == game_category:
                                        game_valid[count] = inventory[i]
                                        count += 1
                        print("Daftar game pada toko yang memenuhi kriteria: ")
                        for i in range(count):
                            print(i+1, end=". ")
                            for j in range (5):
                                print(game_valid[i][j], end=" | ")
                            print()
                    else:
                        for i in range (f_len(inventory)):
                            #Semua Parameter ada (tidak kosong) kecuali ID
                            if game_title == inventory[i][1]:
                                if inventory[i][4] == int(game_price):
                                    if inventory[i][2] == game_category:
                                        if inventory[i][3] == game_year:
                                            game_valid[count] = inventory[i]
                                            count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
    else:
        if game_title == "":
            if game_price == "":
                if game_category == "":
                    if game_year == "":
                        for i in range(f_len(inventory)):
                            #Semua parameter kosong kecuali ID
                            if game_id == inventory[i][0]:
                                game_valid[count] = inventory[i]
                                count += 1
                        if not count == 0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                    else:
                        for i in range (f_len(inventory)):
                            #Parameter ID dan Tahun Rilis ada (tidak kosong)
                            if game_id == inventory[i][0]:
                                if inventory[i][3] == game_year:
                                    game_valid[count] = inventory[i]
                                    count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                else:
                    if game_year == "":
                        for i in range(f_len(inventory)):
                            #Parameter ID dan Kategori ada (tidak kosong)
                            if game_id == inventory[i][0]:
                                if inventory[i][2] == game_category:
                                    game_valid[count] = inventory[i]
                                    count += 1
                        print("Daftar game pada toko yang memenuhi kriteria: ")
                        for i in range(count):
                            print(i+1, end=". ")
                            for j in range (5):
                                print(game_valid[i][j], end=" | ")
                            print()
                    else:
                        for i in range (f_len(inventory)):
                            #Parameter ID, Kategori dan Tahun Rilis ada (tidak kosong)
                            if game_id == inventory[i][0]:
                                if inventory[i][2] == game_category:
                                    if inventory[i][3] == game_year:
                                        game_valid[count] = inventory[i]
                                        count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
            else:
                if game_category == "":
                    if game_year == "":
                        for i in range(f_len(inventory)):
                            #Parameter ID dan Harga tidak kosong
                            if game_id == inventory[i][0]:
                                if int(game_price) == inventory[i][4]:
                                    game_valid[count] = inventory[i]
                                    count += 1
                        if not count == 0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                    else:
                        for i in range (f_len(inventory)):
                            #Parameter tidak kosong kecuali Nama dan Kategori
                            if game_id == inventory[i][0]:
                                if inventory[i][4] == int(game_price):
                                    if inventory[i][3] == game_year:
                                        game_valid[count] = inventory[i]
                                        count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                else:
                    if game_year == "":
                        for i in range(f_len(inventory)):
                            #Parameter tidak kosong kecuali Nama dan Tahun Rilis
                            if game_id == inventory[i][0]:
                                if inventory[i][4] == int(game_price):
                                    if inventory[i][2] == game_category:
                                        game_valid[count] = inventory[i]
                                        count += 1
                        print("Daftar game pada toko yang memenuhi kriteria: ")
                        for i in range(count):
                            print(i+1, end=". ")
                            for j in range (5):
                                print(game_valid[i][j], end=" | ")
                            print()
                    else:
                        for i in range (f_len(inventory)):
                            #Parameter tidak kosong kecuali Nama
                            if game_id == inventory[i][0]:
                                if inventory[i][4] == int(game_price):
                                    if inventory[i][2] == game_category:
                                        if inventory[i][3] == game_year:
                                            game_valid[count] = inventory[i]
                                            count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
        else:
            if game_price == "":
                if game_category == "":
                    if game_year == "":
                        #Parameter ID dan Tahun tidak kosong
                        for i in range(f_len(inventory)):
                            if game_id == inventory[i][0]:
                                if inventory[i][3] == game_year:
                                    game_valid[count] = inventory[i]
                                    count += 1
                        if not count == 0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                    else:
                        for i in range (f_len(inventory)):
                            #Parameter ID, Nama dan Tahun Rilis tidak kosong
                            if game_id == inventory[i][0]:
                                if game_title == inventory[i][1]:
                                    if inventory[i][3] == game_year:
                                        game_valid[count] = inventory[i]
                                        count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                else:
                    if game_year == "":
                        #Parameter ID, Nama dan Kategori tidak kosong
                        for i in range(f_len(inventory)):
                            if game_id == inventory[i][0]:
                                if game_title == inventory[i][1]:
                                    if inventory[i][2] == game_category:
                                        game_valid[count] = inventory[i]
                                        count += 1
                        print("Daftar game pada toko yang memenuhi kriteria: ")
                        for i in range(count):
                            print(i+1, end=". ")
                            for j in range (5):
                                print(game_valid[i][j], end=" | ")
                            print()
                    else:
                        #Parameter Harga kosong
                        for i in range (f_len(inventory)):
                            if game_id == inventory[i][0]:
                                if game_title == inventory[i][1]:
                                    if inventory[i][2] == game_category:
                                        if inventory[i][3] == game_year:
                                            game_valid[count] = inventory[i]
                                            count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
            else:
                if game_category == "":
                    if game_year == "":
                        #Parameter Kategori dan Tahun Rilis kosong
                        for i in range(f_len(inventory)):
                            if game_id == inventory[i][0]:
                                if game_title == inventory[i][1]:
                                    if int(game_price) == inventory[i][4]:
                                        game_valid[count] = inventory[i]
                                        count += 1
                        if not count == 0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                    else:
                        for i in range (f_len(inventory)):
                            #Parameter Kategori Kosong
                            if game_id == inventory[i][0]:
                                if game_title == inventory[i][1]:
                                    if inventory[i][4] == int(game_price):
                                        if inventory[i][3] == game_year:
                                            game_valid[count] = inventory[i]
                                            count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                else:
                    if game_year == "":
                        #Parameter Tahun Rilis kosong
                        for i in range(f_len(inventory)):
                            if game_id == inventory[i][0]:
                                if game_title == inventory[i][1]:
                                    if inventory[i][4] == int(game_price):
                                        if inventory[i][2] == game_category:
                                            game_valid[count] = inventory[i]
                                            count += 1
                        if not count == 0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
                           
                    else:
                        for i in range (f_len(inventory)):
                            #Semua parameter ada (tidak kosong)
                            if game_id == inventory[i][0]:
                                if game_title == inventory[i][1]:
                                    if inventory[i][4] == int(game_price):
                                        if inventory[i][2] == game_category:
                                            if inventory[i][3] == game_year:
                                                game_valid[count] = inventory[i]
                                                count += 1
                        if not count==0:
                            print("Daftar game pada toko yang memenuhi kriteria: ")
                            for i in range(count):
                                print(i+1, end=". ")
                                for j in range (5):
                                    print(game_valid[i][j], end=" | ")
                                print()
                        else:
                            print("Tidak ada game pada toko yang memenuhi kriteria.")
