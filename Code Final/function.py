import support ; import datetime ; import os ; import argparse ; import sys ; import time
# ============================ SUBPROGRAM ==========================
# F02 - Register
def register_user(user):
    # Menambahkan data user baru ke dalam database
    # I.S. matriks data user terdefinisi
    # F.S. matriks data user ditambahkan data user baru
    
    # KAMUS LOKAL
    # nama, username, password = string
    # valid = boolean
    # i = integer
    # register, user = array of array of string
    
    # ALGORITMA
    # input nama, username, password
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    
    # validasi dari input username
    valid = True
    for i in range(support.f_len(username)):
        # validasi karakter yang digunakan dalam username
        if not((ord(username[i]) >= 97 and ord(username[i]) <= 122) or (ord(username[i])>=65 and ord(username[i])<=90) or (ord(username[i])==45) or (ord(username[i])==95) or (ord(username[i])>=48 and ord(username[i])<=57)):
            valid = False
            print("Username",username,"tidak valid, silahkan gunakan username lain.")
    for i in range(support.f_len(user)):
        # validasi keunikan username
        if user[i][1] == username:
            valid = False
            print("Username",username,"sudah terpakai, silahkan gunakan username lain.")

    # jika data sudah valid, data akan dimasukkan ke array "user"
    if valid:
        count = 0
        for i in range(support.f_len(user)):
            if user[i][0][0] == "U":
                count += 1
        id = "User" + str(count+1)
        saldo = "0"
        register = [id,username,nama,password,"User",saldo]
        user = support.f_append(user,register)
        print("Username",username,"telah berhasil register ke dalam Binomo")
    return user

# F03 - Login
def login (user):
    # fungsi yang digunakan pengguna untuk masuk ke dalam sistem

    # KAMUS LOKAL
    # username, pw, user_id, role, saldo = data_user
    # status = boolean
    # i = integer

    # ALGORITMA
    username = input("Masukkan username: ")
    pw = input('Masukkan passsword: ')
    status=False
    user_id = ""
    role = ""
    saldo = "0"
    for i in (user):
        if username == i[1] and pw == i[3]: 
            status=True 
            print(f'Halo {i[2]}! Selamat datang di "Binomo"')
            user_id = i[0]
            role = i[4]
            saldo = i[5]
            return user_id,username,role,saldo,status
    if status == False:
        print('Password atau username salah atau tidak ditemukan.')
        return user_id,username,role,saldo,status

# F04 - Menambahkan game
def add_game(game):
    # Menambahkan data game baru ke dalam database
    # I.S. matriks data game terdefinisi
    # F.S. matriks data game ditambahkan data game baru
    
    # KAMUS LOKAL
    # nama_game, kategori, tahun_rilis, harga_game, stok_awal = string
    # valid = boolean
    # add_game, game = array of array of string

    # Algoritma
    # Menerima input informasi tentang game yang ingin ditambahkan
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga_game = input("Masukkan harga: ")
    stok_awal = input("Masukkan stok awal: ")

    # validasi informasi yang dimasukkan
    valid = False
    while not valid :
        # Meminta input ulang jika input yang diberikan tidak valid
        if nama_game == "" or kategori == "" or tahun_rilis == "" or harga_game == "" or stok_awal == "":
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan di BNMO.")
            nama_game = input("Masukkan nama game: ")
            kategori = input("Masukkan kategori: ")
            tahun_rilis = input("Masukkan tahun rilis: ")
            harga_game = input("Masukkan harga: ")
            stok_awal = input("Masukkan stok awal: ")
        # Data yang dimasukkan sudah valid
        else:
            valid = True
    
    # Mencari tahu ID terakhir dari data yang sudah ada
    count = 0
    if (support.f_len(game)) != 0:
        for i in range(support.f_len(game)):
            if game[i][0][0] == 'G':
                count += 1
    
    # Memberikan ID pada game
    if 0 <= count < 9:
        id_game = "GAME00" + str(count+1)
    elif 9 <= count < 99:
        id_game = "GAME0" + str(count+1)
    elif 99 <= count <= 999:
        id_game = "GAME" + str(count+1)

    # Menyampaikan pesan sukses dan menambahkan informasi ke dalam database game ketika data sudah valid
    if valid:
        print("Selamat! Berhasil menambahkan game",nama_game+".")
        add_game = [id_game,nama_game,kategori,tahun_rilis,harga_game,stok_awal]
        game = support.f_append(game,add_game)
        return game

# F05 - Mengubah Game
def ubah_game (game):
    # prosedur untuk mengganti informasi game pada toko

    # KAMUS LOKAL
    # id_game, nama_game, kategori, tahun_rilis, harga_game = data_game
    # index, index2, i, j = integer

    # ALGORITMA
    id_game=input('Masukkan ID game: ')
    index=-1
    index2=0
    for i in (game):
        if id_game==i[0]:
            index=index2
        index2 += 1       
    nama_game=input('Masukkan nama game: ')
    kategori=input('Masukkan kategori: ')
    tahun_rilis=input('Masukkan tahun rilis: ')
    harga_game=input('Masukkan harga: ')

    if game == []:
        print("Data game pada toko kosong, silahkan minta Admin untuk menambahkan Game pada toko.")
    elif index == -1:
        print("Maaf, game tidak ditemukan.")
    else:
        j=1
        for i in (nama_game,kategori,tahun_rilis,harga_game): 
            if i != '':
                game[index][j]=i 
            j+=1

# F06 - Mengubah stok
def update_stok(role,game):
    # prosedur+ yang digunakan untuk mengubah stok game pada toko
    
    # KAMUS LOKAL
    # id_game = str
    # jumlah = int
    # line = array of data_game
    # found = boolean

    # ALGORITMA
    if role == 'Admin':
        id_game = input('Masukkan ID game: ')
        jumlah = int(input('Masukkan jumlah: '))
        found = False
        
        if game == []:
            print("Data game pada toko kosong, silahkan minta Admin untuk menambahkan Game pada toko.")
        else:
            for line in game:
                if id_game == line[0]:
                    found = True
                    if (int(line[5]) + jumlah) >= 0:
                        line[5] = int(line[5])
                        line[5] += jumlah
                        line[5] = str(line[5])
                        if jumlah >= 0:
                            print('Stok game', line[1], 'berhasil ditambahkan. Stok sekarang:', line[5])
                        else:
                            print('Stok game', line[1], 'berhasil dikurangi. Stok sekarang:', line[5])
                    else:
                        print('Stok game', line[1], 'gagal dikurangi karena stok kurang. Stok sekarang:', line[5])
            if not found:
                print('Tidak ada game dengan ID tersebut')
    else:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.") 
        print("Mintalah ke administrator untuk melakukan hal tersebut.")

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
            for i in range (x, support.f_len(array)):
                if int(array[i][3]) > int(hasil):
                    hasil = array[i][3]
        elif skema == "harga-":
            hasil = list_game[x][4]
            for i in range (x, support.f_len(array)):
                if int(array[i][4]) > int(hasil):
                    hasil = array[i][4]
        return hasil
    
    
    def min (array, skema, x):
        if skema == "tahun+":
            hasil = list_game[x][3]
            for i in range (x, support.f_len(array)):
                if int(array[i][3]) < int(hasil):
                    hasil = array[i][3]
        elif skema == "harga+":
            hasil = list_game[x][4]
            for i in range (x, support.f_len(array)):
                if int(array[i][4]) < int(hasil):
                    hasil = array[i][4]
        elif skema == "" or skema == " ":
                hasil = list_game[x][0]
                for i in range (x, support.f_len(array)):
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
            for i in range (support.f_len(list_game)):
                for j in range (i, support.f_len(list_game)):
                    if list_game[j][4] == max(list_game, skema, i):
                        temp = list_game[j]
                        list_game[j] = list_game[i]
                        list_game[i] = temp
            
            # menampilkan output
            arr_length_max = support.max_length(list_game)
            for i in range(support.f_len(list_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range (5):
                    max_length = arr_length_max[j]
                    length_data = support.f_len(list_game[i][j])
                    print(str(list_game[i][j]) + " "*(max_length-length_data), end = " | ")
                print(list_game[i][5])

        #mengurutkan berdasarkan Tahun Rilis (kecil ke besar)
        elif skema == "tahun-":
            temp = 0
            for i in range (support.f_len(list_game)):
                for j in range (i, support.f_len(list_game)):
                    if list_game[j][3] == max(list_game, skema, i):
                        temp = list_game[j]
                        list_game[j] = list_game[i]
                        list_game[i] = temp
            # menampilkan output
            arr_length_max = support.max_length(list_game)
            for i in range(support.f_len(list_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range (5):
                    max_length = arr_length_max[j]
                    length_data = support.f_len(list_game[i][j])
                    print(str(list_game[i][j]) + " "*(max_length-length_data), end = " | ")
                print(list_game[i][5])

        #mengurutkan berdasarkan Tahun Rilis (besar ke kecil)        
        elif skema == "tahun+":
            temp = 0
            for i in range (support.f_len(list_game)):
                for j in range (i, support.f_len(list_game)):
                    if list_game[j][3] == min(list_game, skema, i):
                        temp = list_game[j]
                        list_game[j] = list_game[i]
                        list_game[i] = temp
            # menampilkan output
            arr_length_max = support.max_length(list_game)
            for i in range(support.f_len(list_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range (5):
                    max_length = arr_length_max[j]
                    length_data = support.f_len(list_game[i][j])
                    print(str(list_game[i][j]) + " "*(max_length-length_data), end = " | ")
                print(list_game[i][5])

        #mengurutkan berdasarkan Harga (besar ke kecil)        
        elif skema == "harga+":
            temp = 0
            for i in range (support.f_len(list_game)):
                for j in range (i, support.f_len(list_game)):
                    if list_game[j][4] == min(list_game, skema, i):
                        temp = list_game[j]
                        list_game[j] = list_game[i]
                        list_game[i] = temp
            # menampilkan output
            arr_length_max = support.max_length(list_game)
            for i in range(support.f_len(list_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range (5):
                    max_length = arr_length_max[j]
                    length_data = support.f_len(list_game[i][j])
                    print(str(list_game[i][j]) + " "*(max_length-length_data), end = " | ")
                print(list_game[i][5])
                
        elif skema == "" or skema == " ":
            temp = 0
            for i in range (support.f_len(list_game)):
                for j in range (i, support.f_len(list_game)):
                    if list_game[j][0] == min(list_game, skema, i):
                        temp = list_game[j]
                        list_game[j] = list_game[i]
                        list_game[i] = temp
            # menampilkan output
            arr_length_max = support.max_length(list_game)
            for i in range(support.f_len(list_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range (5):
                    max_length = arr_length_max[j]
                    length_data = support.f_len(list_game[i][j])
                    print(str(list_game[i][j]) + " "*(max_length-length_data), end = " | ")
                print(list_game[i][5])
            
        #input skema tidak sesuai
        else:
            print("Skema sorting tidak valid!")

# F08 - Membeli game
def buy_game (role, user_id, saldo, game, kepemilikan, temp_history):
    # fungsi yang digunakan oleh User untuk membeli game pada toko

    # KAMUS LOKAL
    # id_game = string
    # new_saldo = int
    # found = bool
    # line = array of data_history, array of data_kepemilikan
    # temp_history = array of data_history
    # kepemilikan = array of data_kepemilikan

    # ALGORITMA
    date = datetime.datetime.now()
    if role == 'User':
        id_game = input('Masukkan ID Game: ')
        found = False

        # melakukan pengecekan pada riwayat pembelian sebelumnya yang belum di save
        for line in temp_history:
            if (id_game == line[0]) and (user_id == line[3]):
                print("Anda sudah memiliki Game tersebut!")
                found = True
                return temp_history, saldo, kepemilikan

        # melakukan pengecekan pada riwayat pembelian sebelumnya yang sudah di save
        for line in kepemilikan :
            if (id_game == line[0]) and (user_id == line[1]):
                print("Anda sudah memiliki Game tersebut!")
                found = True
                return temp_history, saldo, kepemilikan
        if not found: # jika game belum ada dalam riwayat pembelian, maka User bisa membeli game pada toko
            if game == []:
                print("Data game pada toko kosong, silahkan minta Admin untuk menambahkan Game pada toko.")
                return temp_history, saldo, kepemilikan
            else:
                for line in game:
                    if (id_game == line[0]):
                        if (int(line[5]) > 0):
                            if saldo >= int(line[4]):
                                line[5] = int(line[5])
                                found = True
                                new_saldo = saldo - int(line[4])
                                print("Game", line[1], "berhasil dibeli!")
                                line[5] = line[5] - 1
                                line[5] = str(line[5])
                                temp_history = support.f_append(temp_history,[line[0],line[1],line[4],user_id,str(date.year)])
                                kepemilikan = support.f_append(kepemilikan, [line[0],user_id])
                                return temp_history, new_saldo, kepemilikan
                            else:
                                print("Saldo anda tidak cukup untuk membeli game tersebut")
                                found = True
                                return temp_history, saldo, kepemilikan
                        else:
                            print("Stok Game tersebut sedang habis!")
                            found = True
                            return temp_history, saldo, kepemilikan
                if not found :
                    print("Tidak ada Game dengan ID tersebut")
                    return temp_history, saldo, kepemilikan
    else:
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        return temp_history, saldo, kepemilikan

# F09 - Melihat Game yang dimiliki
def list_game(role,user_id,kepemilikan,game):
    # prosedur yang digunakan untuk melihat game yang dimiliki oleh User
    
    # KAMUS LOKAL
    # i, j, max_length, length_data, arr_length_max = integer
    # line = array of data_kepemilikan
    # owned_game_id, my_game = array of data_game

    # ALGORITMA
    if role == "User":
        owned_game_id = []
        my_game = []

        for line in kepemilikan:
                if line[1] == user_id:
                    owned_game_id = support.f_append (owned_game_id,line[0])
        
        if owned_game_id == []:
            print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
        else:
            for i in range(support.f_len(owned_game_id)):
                for line in game:
                    if line[0] == owned_game_id[i]:
                        my_game = support.f_append(my_game,[line[0],line[1],line[2],line[3],line[4]]) # menyimpan data game yang dimiliki pada variabel my_game
            
            # menampilkan output
            arr_length_max = support.max_length(my_game)
            print("Daftar game:")
            for i in range(support.f_len(my_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range(support.f_len(my_game[0])):
                    max_length = arr_length_max[j]
                    length_data = support.f_len(my_game[i][j])
                    if(j == support.f_len(my_game[0])-1):
                        print(my_game[i][j])
                    else:
                        print(str(my_game[i][j]) + " "*(max_length-length_data),end = " | ")
            return
    else:
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        return

# F10 - Mencari Game yang dimiliki dari ID dan tahun rilis
def search_my_game(role,user_id,kepemilikan,game):
    # prosedur yang digunakan user untuk mencari game yang dimiliki berdasarkan ID game dan tahun rilis
    
    # KAMUS LOKAL
    # type data_my_game = <game_id:string, nama:string, harga:string, kategori:string, tahun rilis:string>
    # game_id, tahun_rilis = str
    # count, i, j, max_length, length_data = int
    # line = array of data_kepemilikan, array of data_game
    # owned_game_id = array of string
    # my_game = array of data_my_game

    # ALGORITMA
    if role == "User":
        game_id = input("Masukkan ID Game: ")
        tahun_rilis = input("Masukkan Tahun Rilis Game: ")
        owned_game_id = []
        my_game = []
        count = 0

        for line in kepemilikan:
                if line[1] == user_id:
                    owned_game_id = support.f_append (owned_game_id,line[0])
        # melakukan pengecekan kepemilikan game User
        if owned_game_id == []:
            print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
        else:
            print("Daftar game pada inventory yang memenuhi kriteria:")
            if game_id == "":
                if tahun_rilis == "":
                # jika User tidak memasukan kedua parameter, maka program akan menampilkan seluruh game yang dimiliki oleh User
                    for i in range(support.f_len(owned_game_id)):
                        for line in game:
                            if line[0] == owned_game_id[i]:
                                my_game = support.f_append(my_game,[line[0],line[1],line[4],line[2],line[3]]) # menyimpan data game yang dimiliki pada variabel my_game
                                count += 1
                else: # tahun_rilis != ""
                # jika User hanya memasukan parameter tahun rilis, maka program akan menampilkan seluruh game yang dimiliki oleh User berdasarkan tahun rilisnya
                    for i in range(support.f_len(owned_game_id)):
                        for line in game:
                            if line[0] == owned_game_id[i] and line[3] == tahun_rilis:
                                my_game = support.f_append(my_game,[line[0],line[1],line[4],line[2],line[3]])
                                count += 1

            else: # game_id != ""
                if tahun_rilis == "":
                # jika User hanya memasukan parameter ID Game maka program akan menampilkan seluruh game yang dimiliki oleh User berdasarkan ID Game yang dimasukan
                    for i in range(support.f_len(owned_game_id)):
                        if owned_game_id[i] == game_id:
                            for line in game:
                                if line[0] == owned_game_id[i]:
                                    my_game = support.f_append(my_game,[line[0],line[1],line[4],line[2],line[3]])
                                    count += 1
                else: # tahun_rilis != ""
                # jika User memasukan kedua parameter yang ada maka program akan menampilkan seluruh game yang dimiliki oleh User berdasarkan ID Game dan tahun rilisnya
                    for i in range(support.f_len(owned_game_id)):
                        if owned_game_id[i] == game_id:
                            for line in game:
                                if line[0] == game_id and line[3] == tahun_rilis:
                                    my_game = support.f_append(my_game,[line[0],line[1],line[4],line[2],line[3]])
                                    count += 1

            # menampilkan daftar game yang memenuhi kriteria pencarian berdasarkan parameter
            if count == 0:
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
            else:
                # menampilkan output
                arr_length_max = support.max_length(my_game)
                for i in range(support.f_len(my_game)):
                    if (i < 9):
                        print(i+1, end=".   ")
                    elif(9 <= i < 99):
                        print(i+1, end=".  ")
                    else:
                        print(i+1, end=". ")
                    for j in range(support.f_len(my_game[0])):
                        max_length = arr_length_max[j]
                        length_data = support.f_len(my_game[i][j])
                        if(j == support.f_len(my_game[0])-1):
                            print(my_game[i][j])
                        else:
                            print(str(my_game[i][j]) + " "*(max_length-length_data),end = " | ")
            return

    else:
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        return

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
                            for i in range (support.f_len(inventory)):
                                if inventory[i][3] == game_year:
                                    game_valid = support.f_append(game_valid,inventory[i])
                    else:
                        #Semua parameter kosong kecuali Kategori
                        if game_year == "":
                            for i in range(support.f_len(inventory)):
                                if inventory[i][2] == game_category:
                                    game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            #Parameter Tahun Rilis dan Kategori ada (tidak kosong)
                            for i in range (support.f_len(inventory)):
                                if inventory[i][2] == game_category:
                                    if inventory[i][3] == game_year:
                                        game_valid = support.f_append(game_valid,inventory[i])
                else:
                    if game_category == "":
                        if game_year == "":
                            #Semua parameter kosong kecuali Harga
                            for i in range(support.f_len(inventory)):
                                if game_price == inventory[i][4]:
                                    game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            #Parameter Harga dan Tahun Rilis ada (tidak kosong)
                            for i in range (support.f_len(inventory)):
                                if inventory[i][4] == game_price:
                                    if inventory[i][3] == game_year:
                                        game_valid = support.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            #Parameter Harga dan Kategori ada (tidak kosong)
                            for i in range(support.f_len(inventory)):
                                if inventory[i][4] == game_price:
                                    if inventory[i][2] == game_category:
                                        game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            for i in range (support.f_len(inventory)):
                                #Parameter Harga, Kategori dan Tahun Rilis ada (tidak kosong)
                                if inventory[i][4] == game_price:
                                    if inventory[i][2] == game_category:
                                        if inventory[i][3] == game_year:
                                            game_valid = support.f_append(game_valid,inventory[i])
            else:
                if game_price == "":
                    if game_category == "":
                        if game_year == "":
                            #Semua parameter kosong kecuali Nama
                            for i in range(support.f_len(inventory)):
                                if game_title == inventory[i][1]:
                                    game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            #Parameter Nama dan Tahun Rilis ada (tidak kosong)
                            for i in range (support.f_len(inventory)):
                                if game_title == inventory[i][1]:
                                    if inventory[i][3] == game_year:
                                        game_valid = support.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            #Parameter Nama dan Kategori ada (tidak kosong)
                            for i in range(support.f_len(inventory)):
                                if game_title == inventory[i][1]:
                                    if inventory[i][2] == game_category:
                                        game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            #Parameter Nama, Kategori dan Tahun Rilis ada (tidak kosong)
                            for i in range (support.f_len(inventory)):
                                if game_title == inventory[i][1]:
                                    if inventory[i][2] == game_category:
                                        if inventory[i][3] == game_year:
                                            game_valid = support.f_append(game_valid,inventory[i])
                else:
                    if game_category == "":
                        if game_year == "":
                            #Parameter Nama dan Harga ada (tidak kosong)
                            for i in range(support.f_len(inventory)):
                                if game_title == inventory[i][1]:
                                    if game_price == inventory[i][4]:
                                        game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            for i in range (support.f_len(inventory)):
                                #Parameter Nama, Harga dan Tahun ada (tidak kosong)
                                if game_title == inventory[i][1]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][3] == game_year:
                                            game_valid = support.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            for i in range(support.f_len(inventory)):
                                #Parameter Nama, Harga dan Kategori ada (tidak kosong)
                                if game_title == inventory[i][1]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][2] == game_category:
                                            game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            for i in range (support.f_len(inventory)):
                                #Semua Parameter ada (tidak kosong) kecuali ID
                                if game_title == inventory[i][1]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][2] == game_category:
                                            if inventory[i][3] == game_year:
                                                game_valid = support.f_append(game_valid,inventory[i])
        else:
            if game_title == "":
                if game_price == "":
                    if game_category == "":
                        if game_year == "":
                            for i in range(support.f_len(inventory)):
                                #Semua parameter kosong kecuali ID
                                if game_id == inventory[i][0]:
                                    game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            for i in range (support.f_len(inventory)):
                                #Parameter ID dan Tahun Rilis ada (tidak kosong)
                                if game_id == inventory[i][0]:
                                    if inventory[i][3] == game_year:
                                        game_valid = support.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            for i in range(support.f_len(inventory)):
                                #Parameter ID dan Kategori ada (tidak kosong)
                                if game_id == inventory[i][0]:
                                    if inventory[i][2] == game_category:
                                        game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            for i in range (support.f_len(inventory)):
                                #Parameter ID, Kategori dan Tahun Rilis ada (tidak kosong)
                                if game_id == inventory[i][0]:
                                    if inventory[i][2] == game_category:
                                        if inventory[i][3] == game_year:
                                            game_valid = support.f_append(game_valid,inventory[i])
                else:
                    if game_category == "":
                        if game_year == "":
                            for i in range(support.f_len(inventory)):
                                #Parameter ID dan Harga tidak kosong
                                if game_id == inventory[i][0]:
                                    if game_price == inventory[i][4]:
                                        game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            for i in range (support.f_len(inventory)):
                                #Parameter tidak kosong kecuali Nama dan Kategori
                                if game_id == inventory[i][0]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][3] == game_year:
                                            game_valid = support.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            for i in range(support.f_len(inventory)):
                                #Parameter tidak kosong kecuali Nama dan Tahun Rilis
                                if game_id == inventory[i][0]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][2] == game_category:
                                            game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            for i in range (support.f_len(inventory)):
                                #Parameter tidak kosong kecuali Nama
                                if game_id == inventory[i][0]:
                                    if inventory[i][4] == game_price:
                                        if inventory[i][2] == game_category:
                                            if inventory[i][3] == game_year:
                                                game_valid = support.f_append(game_valid,inventory[i])
            else:
                if game_price == "":
                    if game_category == "":
                        if game_year == "":
                            #Parameter ID dan Nama tidak kosong
                            for i in range(support.f_len(inventory)):
                                if game_id == inventory[i][0]:
                                    if inventory[i][1] == game_title:
                                        game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            for i in range (support.f_len(inventory)):
                                #Parameter ID, Nama dan Tahun Rilis tidak kosong
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][3] == game_year:
                                            game_valid = support.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            #Parameter ID, Nama dan Kategori tidak kosong
                            for i in range(support.f_len(inventory)):
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][2] == game_category:
                                            game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            #Parameter Harga kosong
                            for i in range (support.f_len(inventory)):
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][2] == game_category:
                                            if inventory[i][3] == game_year:
                                                game_valid = support.f_append(game_valid,inventory[i])
                else:
                    if game_category == "":
                        if game_year == "":
                            #Parameter Kategori dan Tahun Rilis kosong
                            for i in range(support.f_len(inventory)):
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if game_price == inventory[i][4]:
                                            game_valid = support.f_append(game_valid,inventory[i])
                        else:
                            for i in range (support.f_len(inventory)):
                                #Parameter Kategori Kosong
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][4] == game_price:
                                            if inventory[i][3] == game_year:
                                                game_valid = support.f_append(game_valid,inventory[i])
                    else:
                        if game_year == "":
                            #Parameter Tahun Rilis kosong
                            for i in range(support.f_len(inventory)):
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][4] == game_price:
                                            if inventory[i][2] == game_category:
                                                game_valid = support.f_append(game_valid,inventory[i])
                            
                        else:
                            for i in range (support.f_len(inventory)):
                                #Semua parameter ada (tidak kosong)
                                if game_id == inventory[i][0]:
                                    if game_title == inventory[i][1]:
                                        if inventory[i][4] == game_price:
                                            if inventory[i][2] == game_category:
                                                if inventory[i][3] == game_year:
                                                    game_valid = support.f_append(game_valid,inventory[i])
    # menampilkan output
    if support.f_len(game_valid) != 0:
        print("Daftar game pada toko yang memenuhi kriteria: ")
        arr_length_max = support.max_length(game_valid)
        for i in range(support.f_len(game_valid)):
            if (i < 9):
                print(i+1, end=".   ")
            elif(9 <= i < 99):
                print(i+1, end=".  ")
            else:
                print(i+1, end=". ")
            for j in range (5):
                max_length = arr_length_max[j]
                length_data = support.f_len(game_valid[i][j])
                print(str(game_valid[i][j]) + " "*(max_length-length_data), end = " | ")
            print(game_valid[i][5])
    else:
        print("Tidak ada game pada toko yang memenuhi kriteria.")

# F12 - Top Up Saldo
def topup(user):
    # Menambahkan data saldo pada user tertentu
    # I.S. matriks data user terdefinisi
    # F.S. perubahan informasi saldo pada data user
    
    # KAMUS LOKAL
    # username = string
    # saldo_tambahan = integer
    # found = Boolean
    # user = array of array of string and integer
    # i = integer

    # ALGORITMA
    # Menerima input username dan saldo tambahan
    username = input("Masukkan username: ")
    saldo_tambahan = int(input("Masukkan saldo: "))

    for i in range(support.f_len(user)):
        user[i][5] = int(user[i][5])
    # Mencari username yang telah diinput di data base
    found = False
    for i in range(support.f_len(user)):
        # Jika username ditemukan, akan dilakukan penambahan saldo
        if user[i][1] == username:
            found = True
            break
    # Jika username tidak ditemukan, akan menyampaikan pesan error
    if found == False:
        print("Username",username,"tidak ditemukan.")
    else:     
    # Validasi saldo tambahan (saldo akhir tidak bisa kurang dari 0)
        if user[i][5] + saldo_tambahan < 0:
            print("Masukkan tidak valid.")
        else:
            if saldo_tambahan >= 0 :
                user[i][5] += saldo_tambahan
                print("Top up berhasil. Saldo",username,"bertambah menjadi",user[i][5])
            else:
                user[i][5] += saldo_tambahan
                print("Top up berhasil. Saldo",username,"berkurang menjadi",user[i][5])

# F13 - Melihat riwayat pembelian
def riwayat_pembelian(riwayatgame,user,username):
    # prosedur yang digunakan user untuk melihat riwayat pembelian game
    
    # KAMUS LOKAL
    # index, index2, arr_length_max, max_length, length_data: integer
    # condition: boolean
    # show_riwayat: array of data_history

    # ALGORITMA
    show_riwayat=[]
    index=0
    index2=0
    for i in (user):
        if i[1]==username:
            index=index2
        index2+=1

    condition=False
    for i in range(support.f_len(riwayatgame)):
        if riwayatgame[i][3]==user[index][0]:
            condition=True
            show_riwayat = support.f_append(show_riwayat,[riwayatgame[i][0],riwayatgame[i][1],riwayatgame[i][2],riwayatgame[i][4]])

    # menampilkan output
    if condition==False:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah buy_game untuk membeli.')
    else:
        print("Daftar game:")
        arr_length_max = support.max_length(show_riwayat)
        for i in range(support.f_len(show_riwayat)):
            if (i < 9):
                print(i+1, end=".   ")
            elif(9 <= i < 99):
                print(i+1, end=".  ")
            else:
                print(i+1, end=". ")
            for j in range(support.f_len(show_riwayat[0])):
                max_length = arr_length_max[j]
                length_data = support.f_len(show_riwayat[i][j])
                if(j == support.f_len(show_riwayat[0])-1):
                    print(show_riwayat[i][j])
                else:
                    print(str(show_riwayat[i][j]) + " "*(max_length-length_data),end = " | ")

# F14 - Help
def help(curr_role):
    # Fungsi menampilkan perintah-perintah yang dapat digunakan pada aplikasi jika belum login/belum ada role tertentu
    
    # KAMUS LOKAL

    # ALGORITMA
    if curr_role == "":
        print("""
        ============ HELP ============
        1. register - Untuk melakukan registrasi user baru
        2. login - Untuk login ke dalam sistem
        3. tambah_game - Untuk menambah game yang dijual pada toko
        4. ubah_game - Untuk mengubah informasi game pada toko
        5. ubah_stok - Untuk mengubah stok game pada toko
        6. list_game_toko - Untuk menampilkan list game pada toko berdasarkan tahun atau harga
        7. buy_game - Untuk membeli game yang tersedia di toko
        8. list_game - Untuk menampilkan daftar game yang dimiliki pengguna
        9. search_my_game - Untuk mencari game yang dimiliki dari ID dan tahun rilis
        10. search_game_at_store - Untuk mencari game di toko dari ID, nama game, harga, kategori, dan tahun rilis
        11. topup - Untuk menambahkan saldo pada pengguna
        12. riwayat - Untuk menampilkan riwayat pembelian game
        13. help - Untuk menampilkan perintah-perintah yang dapat digunakan pada aplikasi
        14. save - Untuk menyimpan perubahan-perubahan yang telah dilakukan
        15. exit - Untuk keluar dari aplikasi
        """)
    
    # Fungsi menampilkan perintah-perintah yang dapat digunakan pada aplikasi jika sudah login dan ada role admin
    elif curr_role == "Admin":
        print("""
        ============ HELP ============
        1. register - Untuk melakukan registrasi user baru
        2. login - Untuk login ke dalam sistem
        3. tambah_game - Untuk menambah game yang dijual pada toko
        4. ubah_game - Untuk mengubah informasi game pada toko
        5. ubah_stok - Untuk mengubah stok game pada toko
        6. list_game_toko - Untuk menampilkan list game pada toko berdasarkan tahun atau harga
        7. search_game_at_store - Untuk mencari game di toko dari ID, nama game, harga, kategori, dan tahun rilis
        8. topup - Untuk menambahkan saldo pada pengguna
        9. help - Untuk menampilkan perintah-perintah yang dapat digunakan pada aplikasi
        10. save - Untuk menyimpan perubahan-perubahan yang telah dilakukan
        11. exit_program - Untuk keluar dari aplikasi
        """)

    # Fungsi menampilkan perintah-perintah yang dapat digunakan pada aplikasi jika sudah login dan ada role user
    elif curr_role == "User":
        print("""
        ============ HELP ============
        1. login - Untuk login ke dalam sistem
        2. list_game_toko - Untuk menampilkan list game pada toko berdasarkan tahun atau harga
        3. buy_game - Untuk membeli game yang tersedia di toko
        4. list_game - Untuk menampilkan daftar game yang dimiliki pengguna
        5. search_my_game - Untuk mencari game yang dimiliki dari ID dan tahun rilis
        6. search_game_at_store - Untuk mencari game di toko dari ID, nama game, harga, kategori, dan tahun rilis
        7. riwayat - Untuk menampilkan riwayat pembelian game
        8. help - Untuk menampilkan perintah-perintah yang dapat digunakan pada aplikasi
        9. save - Untuk menyimpan perubahan-perubahan yang telah dilakukan
        10. exit_program - Untuk keluar dari aplikasi
        """)

# F15 - Load
def load (loaded):
    # fungsi yang digunakan untuk memuat file pada database
    
    # KAMUS LOKAL
    # game = array of data_game
    # user = array of data_user
    # riwayat = array of history
    # kepemilikan = array of data_kepemilikan
    # loaded = bool

    # ALGORITMA
    print('Loading...')
    time.sleep(2)
    if len(sys.argv)!=1:
        parser=argparse.ArgumentParser(usage="")
        parser.add_argument("x")
        args=parser.parse_args()
        namafolder=args.x
        if (os.path.exists(args.x)): 
            game=support.f_open(f"{namafolder}/game.csv")
            user=support.f_open(f"{namafolder}/user.csv")
            riwayat=support.f_open(f"{namafolder}/riwayat.csv")
            kepemilikan=support.f_open(f"{namafolder}/kepemilikan.csv")
            loaded = True
            return (loaded,game,user,riwayat,kepemilikan) 
        else : 
            print (f"folder {args.x} tidak ditemukan")
            loaded = False
            return (loaded,[],[],[],[]) 
    else:
        print ("Tidak ada nama folder yang diberikan!")
        loaded = False
        return (loaded,[],[],[],[]) 

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
    for i in range (support.f_len(game)):
        for j in range (5):
            g.write(str(game[i][j]))
            g.write(";")
        g.write(str(game[i][5]))
        g.write("\n")
    g.close()

    u = open('user.csv', 'w')
    u.write("id;username;nama;password;role;saldo\n")
    for i in range (support.f_len(user)):
        for j in range (5):
            u.write(str(user[i][j]))
            u.write(';')
        u.write(str(user[i][5]))
        u.write('\n')
    u.close()
    
    r = open('riwayat.csv', 'w')
    r.write("game_id;nama;harga;user_id;tahun_beli\n")
    for i in range (support.f_len(riwayat)):
        for j in range (4):
            r.write(str(riwayat[i][j]))
            r.write(';')
        r.write(str(riwayat[i][4]))
        r.write('\n')
    r.close()

    k = open('kepemilikan.csv', 'w')
    k.write("game_id;user_id\n")
    for i in range (support.f_len(kepemilikan)):
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

# F17 - Exit
def exit_program(user, game, riwayat, kepemilikan):
    # fungsi yang digunakan pengguna untuk keluar dari sistem
    # fungsi akan meminta masukan berupa pilihan untuk melakukan perubahan atau tidak

    # KAMUS LOKAL
    # answer = str
    # save(path:string, user:array of data_user, game:array of data_game, riwayat:array of data_history, kepemilikan: array of data_kepemilikan)
    
    # ALGORITMA
    answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while (answer != "y" and answer != "Y" and answer != "n" and answer != "N"):
        answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if (answer == "Y" or answer == 'y'):
        save(user,game,riwayat,kepemilikan)
        print("Terima kasih telah menggunakan Binomo!")
    else:
        print("Data tidak disimpan.")
        print("Terima kasih telah menggunakan Binomo!")
    exit()