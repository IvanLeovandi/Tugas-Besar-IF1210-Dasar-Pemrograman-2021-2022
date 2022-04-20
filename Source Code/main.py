import datetime; import time; import support ; import function

# ============================== MAIN PROGRAM =======================================

# KAMUS GLOBAL
# type data_user : <id:string, username:string, nama:string, password:string, role:string, saldo:integer>
# type data_game : <id:string, nama:string, kategori:string, tahun_rilis:string, harga:integer, stok:integer>
# type data_riwayat : <game_id:string, nama:string, harga:integer, user_id:string, tahun_beli:string>
# type data_kepemilikan : <game_id:string, user_id:string>
# type data_temp_history : <game_id:string, nama:string, harga:integer, kategori:string, tahun_beli:integer>

# user : array of data_user
# game : array of data_game 
# riwayat : array of data_riwayat
# kepemilikan : array of data_kepemilikan
# temp_history : array of data_temp_history

# masih nunggu variabel lainnya


# INISIALISASI
user =[]; game = []; riwayat = []; kepemilikan = []; temp_history = []
user_id = ""

listPerintah = ['register', 'login', 'tambah_game', 'ubah_game', 'ubah_stok', 'list_game_toko', 'buy_game', 'list_game', 
              'list_game', 'search_my_game', 'search_game_at_store', 'topup', 'riwayat', 'save', 'exit']
             
program = True
hasLogin = False
role = ""
username = ""

# Pemanggilan procedure loading()
# directory = load()
load = True

# if not(directory == None):
if load:
    print("Loading...")
    time.sleep(2)
    user = support.f_open("user.csv")
    game = support.f_open("game.csv")
    riwayat = support.f_open("riwayat.csv")
    kepemilikan = support.f_open("kepemilikan.csv")
    print()
    print("Selamat datang di Binomo!")
    print("Pilih menu help untuk menampilkan menu")

    # Jalannya program utama
    while (program):
        command = input(">>> ")
        if command == "help":
            function.help(role)
        elif command == "login":
            if hasLogin:
                print("Anda sudah login, exit terlebih dahulu untuk menggunakan akun lain")
                print()
            else:
                result = function.login(user)
                username = result[0]
                role = result[1]
                saldo = result[2]
                hasLogin = True
        elif command == "exit":
            # Asumsi exit tidak perlu login
            exit()
        else:
            if hasLogin:
                if command == "register":
                    if role == "Admin":
                        user = function.register_user(user)
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "tambah_game":
                    if role == "Admin":
                        game = function.add_game(game)
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "ubah_game":
                    if role == "Admin":
                        function.ubah_game(game)
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "ubah_stok":
                    if role == "Admin":
                        function.update_stok(role,game)
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "list_game_toko":
                    function.list_game_toko(game)
                elif command == "buy_game":
                    hasil = function.buy_game(role,user_id,saldo,game,kepemilikan,temp_history)
                    history = hasil[0]
                    saldo = hasil[1]
                    kepemilikan = hasil[2]
                elif command == "list_game":
                    if role == "User":
                        pass
                        # inventory()
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "search_my_game":
                    function.search_my_game(role,user_id,kepemilikan,game)
                elif command == "search_game_at_store":
                    function.search_game_at_store(game)
                elif command == "topup":
                    if role == "Admin":
                        function.topup(user)
                        # asumsi admin tidak akan mengisi saldo sesama admin
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "riwayat":
                    if role == "User":    
                        function.riwayat_pembelian(riwayat,user,username)
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "game":
                    print(game)
                elif command == "user":
                    print(user)
                elif command == "help":
                    function.help(role)
                elif command == "save":
                    function.save(user,game,riwayat,kepemilikan)
                elif command == "exit_program":
                    function.exit_program(user,game,riwayat,kepemilikan)
                else:
                    # Masukan salah, tidak sesuai keyword yang valid, sudah login
                    print("Input anda tidak valid")
                    print("Berikut merupakan input yang valid")
                    function.help(role)        
            elif support.f_search(listPerintah, command):
                # Masukan benar, tetapi belum login
                print("Anda harus login terlebih dahulu")
                print()
            else:
                # Masukan salah, tidak sesuai keyword yang valid, belum login
                print("Input yang diberikan tidak tersedia")
                print()