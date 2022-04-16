# F06 - Mengubah stok game
def update_stok(role,hasil):
    if role == 'Admin':
        id_game = input('Masukkan ID game: ')
        jumlah = int(input('Masukkan jumlah: '))  
         
        for line in hasil:
            if id_game == line[0]:
                if (line[5] + jumlah) >= 0: 
                    line[5] += jumlah
                    print('Stok game', line[1], 'berhasil ditambahkan. Stok sekarang:', line[5])
                    break
                else:
                    print('Stok game', line[1], 'gagal dikurang karena stok kurang. Stok sekarang:', line[5])
                    break
            else:
                print('Tidak ada game dengan ID tersebut')
                break
    else:
        print('Kamu tidak memiliki akses pada menu ini')

# update_stok('admin', hasil)

# F08 - Beli Game
import datetime

date = datetime.datetime.now()
id_game = input('Masukkan ID Game: ')

def buy (role, id_game, user_id, saldo, game, kepemilikan):
    if role == 'User':
        # history = [open("riwayat.csv")]
        for line in kepemilikan :
            if (id_game == line[0]) and (user_id == line[1]):
                print("Anda sudah memiliki Game tersebut!")
                break
            else:
                for line in game:
                    if (id_game == line[0]):
                        if (line[5] > 0):
                            if saldo > line[4]:
                                saldo -= line[4]
                                print("Game", line[1], "berhasil dibeli!")
                                history = [line[0],line[1],line[4],user_id,date.year]
                                return history, saldo # ini nanti harus dipisahin lagi waktu di main programnya
                                # https://note.nkmk.me/en/python-function-return-multiple-values/#:~:text=Return%20multiple%20values%20using%20commas,the%20return%20%2C%20separated%20by%20commas.
                            else:
                                print("Saldo anda tidak cukup untuk membeli game tersebut")
                                break
                        else:
                            print("Stok Game tersebut sedang habis!")
                            break
                    else:
                        print("Tidak ada Game dengan ID tersebut")
                        break

    else:
        print("Anda tidak memiliki akses pada menu ini.")



# F10 - Mencari game yang dimiliki
def search_my_game(role, user_id,kepemilikan):
    if role == "User":
        game_id = input("Masukkan ID Game: ")
        tahun_rilis = input("Masukkan Tahun Rilis Game: ")
        for line in kepemilikan:
            pass

# F17 - Exit
def exit(hasil):
    answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while (answer != "y" or answer != "Y" or answer != "n" or answer != "N"):
        answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if (answer == "Y" or answer == 'y'):
        # save()
        print("Data berhasil disimpan.")
        print("Anda telah keluar dari program.")
    else:
        print("Data tidak disimpan.")
        print("Anda telah keluar dari program.")
    # close()