import f_len ; import f_append ; import f_max_length ; import os ; import time
# F07 - List Game toko
def list_game_toko(game):
    # prosedur untuk mengurutkan game berdasarkan masukan skema yang diinginkan

    # KAMUS LOKAL
    # list_game = array of (array of string)
    # skema = string
    # temp = string

    # ALGORITMA
    def max (array, skema, x):
        if skema == "tahun-":
            hasil = list_game[x][3]
            for i in range (x, f_len.f_len(array)):
                if int(array[i][3]) > int(hasil):
                    hasil = array[i][3]
        elif skema == "harga-":
            hasil = list_game[x][4]
            for i in range (x, f_len.f_len(array)):
                if int(array[i][4]) > int(hasil):
                    hasil = array[i][4]
        return hasil
    
    
    def min (array, skema, x):
        if skema == "tahun+":
            hasil = list_game[x][3]
            for i in range (x, f_len.f_len(array)):
                if int(array[i][3]) < int(hasil):
                    hasil = array[i][3]
        elif skema == "harga+":
            hasil = list_game[x][4]
            for i in range (x, f_len.f_len(array)):
                if int(array[i][4]) < int(hasil):
                    hasil = array[i][4]
        elif skema == "" or skema == " ":
                hasil = list_game[x][0]
                for i in range (x, f_len.f_len(array)):
                    if get_id(array[i][0]) < (get_id(hasil)):
                        hasil = array[i][0]
        return hasil

    def get_id (game_id):
        hasil = game_id[4]*100 + game_id[5]*10 + game_id[6]
        return hasil

    list_game = game
    skema = input("Skema sorting : ")
    if game == []:
        print("Data game pada toko kosong, silahkan minta Admin untuk menambahkan Game pada toko.")
    else:
        #mengurutkan berdasarkan Harga (kecil ke besar)
        if skema == "harga-":
            temp = 0
            for i in range (f_len.f_len(list_game)):
                for j in range (i, f_len.f_len(list_game)):
                    if list_game[j][4] == max(list_game, skema, i):
                        temp = list_game[j]
                        list_game[j] = list_game[i]
                        list_game[i] = temp
            
            # menampilkan output
            arr_length_max = f_max_length.max_length(list_game)
            for i in range(f_len.f_len(list_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range (5):
                    max_length = arr_length_max[j]
                    length_data = f_len.f_len(list_game[i][j])
                    print(str(list_game[i][j]) + " "*(max_length-length_data), end = " | ")
                print(list_game[i][5])

        #mengurutkan berdasarkan Tahun Rilis (kecil ke besar)
        elif skema == "tahun-":
            temp = 0
            for i in range (f_len.f_len(list_game)):
                for j in range (i, f_len.f_len(list_game)):
                    if list_game[j][3] == max(list_game, skema, i):
                        temp = list_game[j]
                        list_game[j] = list_game[i]
                        list_game[i] = temp
            # menampilkan output
            arr_length_max = f_max_length.max_length(list_game)
            for i in range(f_len.f_len(list_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range (5):
                    max_length = arr_length_max[j]
                    length_data = f_len.f_len(list_game[i][j])
                    print(str(list_game[i][j]) + " "*(max_length-length_data), end = " | ")
                print(list_game[i][5])

        #mengurutkan berdasarkan Tahun Rilis (besar ke kecil)        
        elif skema == "tahun+":
            temp = 0
            for i in range (f_len.f_len(list_game)):
                for j in range (i, f_len.f_len(list_game)):
                    if list_game[j][3] == min(list_game, skema, i):
                        temp = list_game[j]
                        list_game[j] = list_game[i]
                        list_game[i] = temp
            # menampilkan output
            arr_length_max = f_max_length.max_length(list_game)
            for i in range(f_len.f_len(list_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range (5):
                    max_length = arr_length_max[j]
                    length_data = f_len.f_len(list_game[i][j])
                    print(str(list_game[i][j]) + " "*(max_length-length_data), end = " | ")
                print(list_game[i][5])

        #mengurutkan berdasarkan Harga (besar ke kecil)        
        elif skema == "harga+":
            temp = 0
            for i in range (f_len.f_len(list_game)):
                for j in range (i, f_len.f_len(list_game)):
                    if list_game[j][4] == min(list_game, skema, i):
                        temp = list_game[j]
                        list_game[j] = list_game[i]
                        list_game[i] = temp
            # menampilkan output
            arr_length_max = f_max_length.max_length(list_game)
            for i in range(f_len.f_len(list_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range (5):
                    max_length = arr_length_max[j]
                    length_data = f_len.f_len(list_game[i][j])
                    print(str(list_game[i][j]) + " "*(max_length-length_data), end = " | ")
                print(list_game[i][5])
                
        elif skema == "" or skema == " ":
            temp = 0
            for i in range (f_len.f_len(list_game)):
                for j in range (i, f_len.f_len(list_game)):
                    if list_game[j][0] == min(list_game, skema, i):
                        temp = list_game[j]
                        list_game[j] = list_game[i]
                        list_game[i] = temp
            # menampilkan output
            arr_length_max = f_max_length.max_length(list_game)
            for i in range(f_len.f_len(list_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range (5):
                    max_length = arr_length_max[j]
                    length_data = f_len.f_len(list_game[i][j])
                    print(str(list_game[i][j]) + " "*(max_length-length_data), end = " | ")
                print(list_game[i][5])
            
        #input skema tidak sesuai
        else:
            print("Skema sorting tidak valid!")

# F11 - Mencari Game di toko
def search_game_at_store(game):
    # prosedur untuk mencari game pada toko berdasarkan kategori pencarian
    
    # KAMUS LOKAL
    # inventory = array of (array of string)
    # game_valid = array of (array of string)
    # game_id = string
    # game_title = string
    # game_price = string
    # game_category = string
    # game_year = string
    # count, i = integer

    # ALGORITMA
    inventory = game
    game_id = input("Masukkan ID Game: ")
    game_title = input("Masukkan Nama Game: ")
    game_price = input("Masukkan Harga Game: ")
    game_category = input("Masukkan kategori game: ")
    game_year = input("Masukkan Tahun Rilis Game: ")
    game_valid = []

    if game == []:
        print("Data game pada toko kosong, silahkan minta Admin untuk menambahkan Game pada toko.")
    else:
        if game_id == "":
            if game_title == "":
                if game_price == "":
                    if game_category == "":
                        if game_year == "":
                            #Semua parameter kosong
                            game_valid = inventory
                        else:
                            #Semua paramater kosong kecuali Tahun Rilis
                            for i in range (f_len.f_len(inventory)):
                                if inventory[i][3] == game_year:
                                    game_valid = f_append.f_append(game_valid,inventory[i])
                    else:
                        #Semua parameter kosong kecuali Kategori
                        if game_year == "":
                            for i in range(f_len.f_len(inventory)):
                                if inventory[i][2] == game_category:
                                    game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            #Parameter Tahun Rilis dan Kategori ada (tidak kosong)
                            for i in range (f_len.f_len(inventory)):
                                if inventory[i][2] == game_category:
                                    if inventory[i][3] == game_year:
                                        game_valid = f_append.f_append(game_valid,inventory[i])
                else:
                    if game_category == "":
                        if game_year == "":
                            #Semua parameter kosong kecuali Harga
                            for i in range(f_len.f_len(inventory)):
                                if game_price == inventory[i][4]:
                                    game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            #Parameter Harga dan Tahun Rilis ada (tidak kosong)
                            for i in range (f_len.f_len(inventory)):
                                if inventory[i][4] == game_price:
                                    if inventory[i][3] == game_year:
                                        game_valid = f_append.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            #Parameter Harga dan Kategori ada (tidak kosong)
                            for i in range(f_len.f_len(inventory)):
                                if inventory[i][4] == game_price:
                                    if inventory[i][2] == game_category:
                                        game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            for i in range (f_len.f_len(inventory)):
                                #Parameter Harga, Kategori dan Tahun Rilis ada (tidak kosong)
                                if inventory[i][4] == game_price:
                                    if inventory[i][2] == game_category:
                                        if inventory[i][3] == game_year:
                                            game_valid = f_append.f_append(game_valid,inventory[i])
            else:
                if game_price == "":
                    if game_category == "":
                        if game_year == "":
                            #Semua parameter kosong kecuali Nama
                            for i in range(f_len.f_len(inventory)):
                                if game_title == inventory[i][1]:
                                    game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            #Parameter Nama dan Tahun Rilis ada (tidak kosong)
                            for i in range (f_len.f_len(inventory)):
                                if game_title == inventory[i][1]:
                                    if inventory[i][3] == game_year:
                                        game_valid = f_append.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            #Parameter Nama dan Kategori ada (tidak kosong)
                            for i in range(f_len.f_len(inventory)):
                                if game_title == inventory[i][1]:
                                    if inventory[i][2] == game_category:
                                        game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            #Parameter Nama, Kategori dan Tahun Rilis ada (tidak kosong)
                            for i in range (f_len.f_len(inventory)):
                                if game_title == inventory[i][1]:
                                    if inventory[i][2] == game_category:
                                        if inventory[i][3] == game_year:
                                            game_valid = f_append.f_append(game_valid,inventory[i])
                else:
                    if game_category == "":
                        if game_year == "":
                            #Parameter Nama dan Harga ada (tidak kosong)
                            for i in range(f_len.f_len(inventory)):
                                if game_title == inventory[i][1]:
                                    if game_price == inventory[i][4]:
                                        game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            for i in range (f_len.f_len(inventory)):
                                #Parameter Nama, Harga dan Tahun ada (tidak kosong)
                                if game_title == inventory[i][1]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][3] == game_year:
                                            game_valid = f_append.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            for i in range(f_len.f_len(inventory)):
                                #Parameter Nama, Harga dan Kategori ada (tidak kosong)
                                if game_title == inventory[i][1]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][2] == game_category:
                                            game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            for i in range (f_len.f_len(inventory)):
                                #Semua Parameter ada (tidak kosong) kecuali ID
                                if game_title == inventory[i][1]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][2] == game_category:
                                            if inventory[i][3] == game_year:
                                                game_valid = f_append.f_append(game_valid,inventory[i])
        else:
            if game_title == "":
                if game_price == "":
                    if game_category == "":
                        if game_year == "":
                            for i in range(f_len.f_len(inventory)):
                                #Semua parameter kosong kecuali ID
                                if game_id == inventory[i][0]:
                                    game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            for i in range (f_len.f_len(inventory)):
                                #Parameter ID dan Tahun Rilis ada (tidak kosong)
                                if game_id == inventory[i][0]:
                                    if inventory[i][3] == game_year:
                                        game_valid = f_append.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            for i in range(f_len.f_len(inventory)):
                                #Parameter ID dan Kategori ada (tidak kosong)
                                if game_id == inventory[i][0]:
                                    if inventory[i][2] == game_category:
                                        game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            for i in range (f_len.f_len(inventory)):
                                #Parameter ID, Kategori dan Tahun Rilis ada (tidak kosong)
                                if game_id == inventory[i][0]:
                                    if inventory[i][2] == game_category:
                                        if inventory[i][3] == game_year:
                                            game_valid = f_append.f_append(game_valid,inventory[i])
                else:
                    if game_category == "":
                        if game_year == "":
                            for i in range(f_len.f_len(inventory)):
                                #Parameter ID dan Harga tidak kosong
                                if game_id == inventory[i][0]:
                                    if game_price == inventory[i][4]:
                                        game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            for i in range (f_len.f_len(inventory)):
                                #Parameter tidak kosong kecuali Nama dan Kategori
                                if game_id == inventory[i][0]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][3] == game_year:
                                            game_valid = f_append.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            for i in range(f_len.f_len(inventory)):
                                #Parameter tidak kosong kecuali Nama dan Tahun Rilis
                                if game_id == inventory[i][0]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][2] == game_category:
                                            game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            for i in range (f_len.f_len(inventory)):
                                #Parameter tidak kosong kecuali Nama
                                if game_id == inventory[i][0]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][2] == game_category:
                                            if inventory[i][3] == game_year:
                                                game_valid = f_append.f_append(game_valid,inventory[i])
            else:
                if game_price == "":
                    if game_category == "":
                        if game_year == "":
                            #Parameter ID dan Nama tidak kosong
                            for i in range(f_len.f_len(inventory)):
                                if game_id == inventory[i][0]:
                                    if inventory[i][1] == game_title:
                                        game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            for i in range (f_len.f_len(inventory)):
                                #Parameter ID, Nama dan Tahun Rilis tidak kosong
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][3] == game_year:
                                            game_valid = f_append.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            #Parameter ID, Nama dan Kategori tidak kosong
                            for i in range(f_len.f_len(inventory)):
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][2] == game_category:
                                            game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            #Parameter Harga kosong
                            for i in range (f_len.f_len(inventory)):
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][2] == game_category:
                                            if inventory[i][3] == game_year:
                                                game_valid = f_append.f_append(game_valid,inventory[i])
                else:
                    if game_category == "":
                        if game_year == "":
                            #Parameter Kategori dan Tahun Rilis kosong
                            for i in range(f_len.f_len(inventory)):
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if game_price == inventory[i][4]:
                                            game_valid = f_append.f_append(game_valid,inventory[i])
                        else:
                            for i in range (f_len.f_len(inventory)):
                                #Parameter Kategori Kosong
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][4] == game_price:
                                            if inventory[i][3] == game_year:
                                                game_valid = f_append.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            #Parameter Tahun Rilis kosong
                            for i in range(f_len.f_len(inventory)):
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][4] == game_price:
                                            if inventory[i][2] == game_category:
                                                game_valid = f_append.f_append(game_valid,inventory[i])
                            
                        else:
                            for i in range (f_len.f_len(inventory)):
                                #Semua parameter ada (tidak kosong)
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][4] == game_price:
                                            if inventory[i][2] == game_category:
                                                if inventory[i][3] == game_year:
                                                    game_valid = f_append.f_append(game_valid,inventory[i])
    # menampilkan output
    if f_len.f_len(game_valid) != 0:
        print("Daftar game pada toko yang memenuhi kriteria: ")
        arr_length_max = f_max_length.max_length(game_valid)
        for i in range(f_len.f_len(game_valid)):
            if (i < 9):
                print(i+1, end=".   ")
            elif(9 <= i < 99):
                print(i+1, end=".  ")
            else:
                print(i+1, end=". ")
            for j in range (5):
                max_length = arr_length_max[j]
                length_data = f_len.f_len(game_valid[i][j])
                print(str(game_valid[i][j]) + " "*(max_length-length_data), end = " | ")
            print(game_valid[i][5])
    else:
        print("Tidak ada game pada toko yang memenuhi kriteria.")

# F16 - Save
def save(user,game,riwayat,kepemilikan):
    # prosedur yang digunakan untuk menyimpan perubahan

    # KAMUS LOKAL
    # g : SEQFILE of 
    #     (*)data_game
    #     (1)"" 
    # u : SEQFILE of 
    #     (*)data_user
    #     (1)""
    # r : SEQFILE of 
    #     (*)data_riwayat
    #     (1)""
    # k : SEQFILE of 
    #     (*)data_kepemilikan
    #     (1)""
    # current_path, path : string

    # ALGORITMA
    current_path = os.getcwd()
    path = input('Masukkan nama folder penyimpanan: ')
    if not os.path.exists(path):
        os.mkdir(path)

    os.chdir(path)

    g = open('game.csv', 'w')
    g.write("id;nama;kategori;tahun_rilis;harga;stok\n")
    for i in range (f_len.f_len(game)):
        for j in range (5):
            g.write(str(game[i][j]))
            g.write(";")
        g.write(str(game[i][5]))
        g.write("\n")
    g.close()

    u = open('user.csv', 'w')
    u.write("id;username;nama;password;role;saldo\n")
    for i in range (f_len.f_len(user)):
        for j in range (5):
            u.write(str(user[i][j]))
            u.write(';')
        u.write(str(user[i][5]))
        u.write('\n')
    u.close()
    
    r = open('riwayat.csv', 'w')
    r.write("game_id;nama;harga;user_id;tahun_beli\n")
    for i in range (f_len.f_len(riwayat)):
        for j in range (4):
            r.write(str(riwayat[i][j]))
            r.write(';')
        r.write(str(riwayat[i][4]))
        r.write('\n')
    r.close()

    k = open('kepemilikan.csv', 'w')
    k.write("game_id;user_id\n")
    for i in range (f_len.f_len(kepemilikan)):
        for j in range (1):
            k.write(str(kepemilikan[i][j]))
            k.write(';')
        k.write(str(kepemilikan[i][1]))
        k.write('\n')
    k.close()

    os.chdir(current_path)
    print("Saving...")
    time.sleep(2)
    print("Data berhasil disimpan pada", path)