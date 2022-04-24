import ivan ; import hosea ; import petrus ; import sultan ; import f_search

# ============================== MAIN PROGRAM =======================================

# KAMUS GLOBAL
# type data_user : <id:string, username:string, nama:string, password:string, role:string, saldo:integer>
# type data_game : <id:string, nama:string, kategori:string, tahun_rilis:string, harga:integer, stok:integer>
# type data_history : <id_game:string, nama:string, harga:integer, user_id:string, tahun_beli:string>
# type data_kepemilikan : <id_game:string, user_id:string>
# list_command : array of string

# user : array of data_user
# game : array of data_game 
# riwayat : array of data_history
# kepemilikan : array of data_kepemilikan

# INISIALISASI
user =[]; game = []; riwayat = []; kepemilikan = []

list_command = ['register', 'tambah_game', 'ubah_game', 'ubah_stok', 'list_game_toko', 'buy_game', 'list_game', 
               'search_my_game', 'search_game_at_store', 'topup', 'riwayat', 'save', 'exit']  

user_id = ""
username = ""
role = ""

program = True
hasLogin = False

# Pemanggilan function load()
loaded = False

if not loaded:
    loaded_file = sultan.load(loaded)
    loaded = loaded_file[0]
    game = loaded_file[1]
    user = loaded_file[2]
    riwayat = loaded_file[3]
    kepemilikan = loaded_file[4]

if loaded:
    print()
    print("Selamat datang di Binomo!")
    print("Pilih menu help untuk menampilkan menu")
    while (program):
        command = input(">>> ")
        if command == "help":
            hosea.help(role)
        elif command == "login":
            if hasLogin:
                print("Anda sudah login, exit terlebih dahulu untuk menggunakan akun lain")
            else:
                result = sultan.login(user)
                user_id = result[0]
                username = result[1]
                role = result[2]
                saldo = int(result[3])
                hasLogin = result[4]
        elif command == "exit":
            # Asumsi exit tidak perlu login
            exit()
        else:
            if hasLogin:
                if command == "register":
                    if role == "Admin":
                        user = hosea.register_user(user)
                    else:
                        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.") 
                        print("Mintalah ke administrator untuk melakukan hal tersebut.")
                elif command == "tambah_game":
                    if role == "Admin":
                        game = hosea.add_game(game)
                    else:
                        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.") 
                        print("Mintalah ke administrator untuk melakukan hal tersebut.")
                elif command == "ubah_game":
                    if role == "Admin":
                        sultan.ubah_game(game)
                    else:
                        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.") 
                        print("Mintalah ke administrator untuk melakukan hal tersebut.")
                elif command == "ubah_stok":
                    if role == "Admin":
                        ivan.update_stok(role,game)
                    else:
                        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.") 
                        print("Mintalah ke administrator untuk melakukan hal tersebut.")
                elif command == "list_game_toko":
                    petrus.list_game_toko(game)
                elif command == "buy_game":
                    hasil = ivan.buy_game(role,user_id,saldo,game,kepemilikan,riwayat)
                    riwayat = hasil[0]
                    saldo = hasil[1]
                    kepemilikan = hasil[2]
                elif command == "list_game":
                    ivan.list_game(role,user_id,kepemilikan,game)
                elif command == "search_my_game":
                    ivan.search_my_game(role,user_id,kepemilikan,game)
                elif command == "search_game_at_store":
                    petrus.search_game_at_store(game)
                elif command == "topup":
                    if role == "Admin":
                        hosea.topup(user)
                        # Asumsi admin tidak akan mengisi saldo sesama admin
                    else:
                        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.") 
                        print("Mintalah ke administrator untuk melakukan hal tersebut.")
                elif command == "riwayat":
                    if role == "User":   
                        sultan.riwayat_pembelian(riwayat,user,username) # antara pake riwayat.csv atau variabel temp_history
                    else:
                        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                elif command == "help":
                    hosea.help(role)
                elif command == "save":
                    for line in user:
                        if line[0] == user_id:
                            line[5] = str(saldo)
                    petrus.save(user,game,riwayat,kepemilikan)
                elif command == "exit_program":
                    ivan.exit_program(user,game,riwayat,kepemilikan)
                else:
                    # Masukan salah, tidak sesuai keyword yang valid, sudah login
                    print("Input anda tidak valid")
                    hosea.help(role)        
            elif f_search.f_search(list_command, command):
                # Masukan benar, tetapi belum login
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')
            else:
                # Masukan salah, tidak sesuai keyword yang valid, belum login
                print("Input yang diberikan tidak tersedia")