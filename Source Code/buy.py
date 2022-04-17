import datetime

date = datetime.datetime.now()
id_game = input('Masukkan ID Game: ')

def buy (role, id_game, user_id, saldo, game, kepemilikan, history):
    if role == 'User':
        found = False

        for line in history:
            if (id_game == line[0]) and (user_id == line[3]):
                print("Anda sudah memiliki Game tersebut!")
                found = True
                return history, saldo

        for line in kepemilikan :
            if (id_game == line[0]) and (user_id == line[1]):
                print("Anda sudah memiliki Game tersebut!")
                found = True
                return history, saldo
            else:
                for line in game:
                    if (id_game == line[0]):
                        if (int(line[5]) > 0):
                            if saldo > int(line[4]):
                                new_saldo = saldo - int(line[4])
                                print("Game", line[1], "berhasil dibeli!")
                                history = f_append(history,[line[0],line[1],line[4],user_id,date.year])
                                found = True
                                line[5] = int(line[5]) - 1
                                return history, new_saldo # ini nanti harus dipisahin lagi waktu di main programnya
                                # https://note.nkmk.me/en/python-function-return-multiple-values/#:~:text=Return%20multiple%20values%20using%20commas,the%20return%20%2C%20separated%20by%20commas.
                            else:
                                print("Saldo anda tidak cukup untuk membeli game tersebut")
                                found = True
                                return history, saldo
                        else:
                            print("Stok Game tersebut sedang habis!")
                            found = True
                            return history, saldo
                if not found :
                    print("Tidak ada Game dengan ID tersebut")
                    return history, saldo
    else:
        print("Anda tidak memiliki akses pada menu ini.")
