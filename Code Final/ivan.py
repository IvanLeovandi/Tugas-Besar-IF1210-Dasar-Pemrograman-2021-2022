import f_len ; import f_append ; import f_max_length ; import datetime ; import petrus

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
                                temp_history = f_append.f_append(temp_history,[line[0],line[1],line[4],user_id,str(date.year)])
                                kepemilikan = f_append.f_append(kepemilikan, [line[0],user_id])
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
                    owned_game_id = f_append.f_append (owned_game_id,line[0])
        
        if owned_game_id == []:
            print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
        else:
            for i in range(f_len.f_len(owned_game_id)):
                for line in game:
                    if line[0] == owned_game_id[i]:
                        my_game = f_append.f_append(my_game,[line[0],line[1],line[2],line[3],line[4]]) # menyimpan data game yang dimiliki pada variabel my_game
            
            # menampilkan output
            arr_length_max = f_max_length.max_length(my_game)
            print("Daftar game:")
            for i in range(f_len.f_len(my_game)):
                if (i < 9):
                    print(i+1, end=".   ")
                elif(9 <= i < 99):
                    print(i+1, end=".  ")
                else:
                    print(i+1, end=". ")
                for j in range(f_len.f_len(my_game[0])):
                    max_length = arr_length_max[j]
                    length_data = f_len.f_len(my_game[i][j])
                    if(j == f_len.f_len(my_game[0])-1):
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
                    owned_game_id = f_append.f_append (owned_game_id,line[0])
        # melakukan pengecekan kepemilikan game User
        if owned_game_id == []:
            print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
        else:
            print("Daftar game pada inventory yang memenuhi kriteria:")
            if game_id == "":
                if tahun_rilis == "":
                # jika User tidak memasukan kedua parameter, maka program akan menampilkan seluruh game yang dimiliki oleh User
                    for i in range(f_len.f_len(owned_game_id)):
                        for line in game:
                            if line[0] == owned_game_id[i]:
                                my_game = f_append.f_append(my_game,[line[0],line[1],line[4],line[2],line[3]]) # menyimpan data game yang dimiliki pada variabel my_game
                                count += 1
                else: # tahun_rilis != ""
                # jika User hanya memasukan parameter tahun rilis, maka program akan menampilkan seluruh game yang dimiliki oleh User berdasarkan tahun rilisnya
                    for i in range(f_len.f_len(owned_game_id)):
                        for line in game:
                            if line[0] == owned_game_id[i] and line[3] == tahun_rilis:
                                my_game = f_append.f_append(my_game,[line[0],line[1],line[4],line[2],line[3]])
                                count += 1

            else: # game_id != ""
                if tahun_rilis == "":
                # jika User hanya memasukan parameter ID Game maka program akan menampilkan seluruh game yang dimiliki oleh User berdasarkan ID Game yang dimasukan
                    for i in range(f_len.f_len(owned_game_id)):
                        if owned_game_id[i] == game_id:
                            for line in game:
                                if line[0] == owned_game_id[i]:
                                    my_game = f_append.f_append(my_game,[line[0],line[1],line[4],line[2],line[3]])
                                    count += 1
                else: # tahun_rilis != ""
                # jika User memasukan kedua parameter yang ada maka program akan menampilkan seluruh game yang dimiliki oleh User berdasarkan ID Game dan tahun rilisnya
                    for i in range(f_len.f_len(owned_game_id)):
                        if owned_game_id[i] == game_id:
                            for line in game:
                                if line[0] == game_id and line[3] == tahun_rilis:
                                    my_game = f_append.f_append(my_game,[line[0],line[1],line[4],line[2],line[3]])
                                    count += 1

            # menampilkan daftar game yang memenuhi kriteria pencarian berdasarkan parameter
            if count == 0:
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
            else:
                # menampilkan output
                arr_length_max = f_max_length.max_length(my_game)
                for i in range(f_len.f_len(my_game)):
                    if (i < 9):
                        print(i+1, end=".   ")
                    elif(9 <= i < 99):
                        print(i+1, end=".  ")
                    else:
                        print(i+1, end=". ")
                    for j in range(f_len.f_len(my_game[0])):
                        max_length = arr_length_max[j]
                        length_data = f_len.f_len(my_game[i][j])
                        if(j == f_len.f_len(my_game[0])-1):
                            print(my_game[i][j])
                        else:
                            print(str(my_game[i][j]) + " "*(max_length-length_data),end = " | ")
            return

    else:
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        return

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
        petrus.save(user,game,riwayat,kepemilikan)
        print("Terima kasih telah menggunakan Binomo!")
    else:
        print("Data tidak disimpan.")
        print("Terima kasih telah menggunakan Binomo!")
    exit()