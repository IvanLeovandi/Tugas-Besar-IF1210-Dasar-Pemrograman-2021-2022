def search_my_game(role,user_id,kepemilikan,game):
    if role == "User":
        game_id = input("Masukkan ID Game: ")
        tahun_rilis = input("Masukkan Tahun Rilis Game: ")
        owned_game_id = []
        my_game = []
        count = 0

        for line in kepemilikan:
                if line[1] == user_id:
                    owned_game_id = f_append (owned_game_id,line[0])

        print("Daftar game pada inventory yang memenuhi kriteria:")
        if game_id == "":
            if tahun_rilis == "":
            # jika User tidak memasukan kedua parameter, maka program akan menampilkan seluruh game yang dimiliki oleh User
                for i in range(f_len(owned_game_id)):
                    for line in game:
                        if line[0] == owned_game_id[i]:
                            my_game = f_append(my_game,[line[0],line[1],line[4],line[2],line[3]]) # menyimpan data game yang dimiliki pada variabel my_game
                            count += 1
            else: # tahun_rilis != ""
            # jika User hanya memasukan parameter tahun rilis, maka program akan menampilkan seluruh game yang dimiliki oleh User berdasarkan tahun rilisnya
                for i in range(f_len(owned_game_id)):
                    for line in game:
                        if line[0] == owned_game_id[i] and line[3] == tahun_rilis:
                            my_game = f_append(my_game,[line[0],line[1],line[4],line[2],line[3]])
                            count += 1

        else: # game_id != ""
            if tahun_rilis == "":
            # jika User hanya memasukan parameter ID Game maka program akan menampilkan seluruh game yang dimiliki oleh User berdasarkan ID Game yang dimasukan
                for i in range(f_len(owned_game_id)):
                    if owned_game_id[i] == game_id:
                        for line in game:
                            if line[0] == owned_game_id[i]:
                                my_game = f_append(my_game,[line[0],line[1],line[4],line[2],line[3]])
                                count += 1
            else: # tahun_rilis != ""
            # jika User memasukan kedua parameter yang ada maka program akan menampilkan seluruh game yang dimiliki oleh User berdasarkan ID Game dan tahun rilisnya
                for i in range(f_len(owned_game_id)):
                    if owned_game_id[i] == game_id:
                        for line in game:
                            if line[0] == game_id and line[3] == tahun_rilis:
                                my_game = f_append(my_game,[line[0],line[1],line[4],line[2],line[3]])
                                count += 1

        # menampilkan daftar game yang memenuhi kriteria pencarian berdasarkan parameter
        if count == 0:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        else:
            nomor = 1
            for line in my_game:
                print(str(nomor) + ". " + str(line[0]) + " | " + str(line[1]) + " | " + str(line[4]) + " | " + str(line[2]) + " | " + str(line[3]))
                nomor += 1
        return

    else:
        print("Anda tidak memiliki akses pada menu ini")
        return