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
user_id = ""; saldo = 0

# lstPerintah = ['register', 'login', 'carirarity', 'caritahun', 'tambahitem', 'hapusitem', 'ubahjumlah', 'pinjam', 
             # 'kembalikan', 'minta', 'riwayatpinjam', 'riwayatkembali', 'riwayatambil', 'save', 'help', 'gacha']
             
program = True
hasLogin = False
isAdmin = False

# Pemanggilan procedure loading()
directory = loading()

if not(directory == None):
    print("Loading...")
    time.sleep(2)
    load(directory)
    print()
    print("Selamat datang di Binomo!")

    # Jalannya program utama
    while (program):
        # help()
        command = input(">>> ")
        if command == "register":
            register()
        elif command == "login":
            if hasLogin:
                print("Anda sudah login, exit terlebih dahulu untuk menggunakan akun lain")
                print()
            else:
                login()
                print('Halo ' + nama + '! Selamat datang di "Binomo"')
        elif command == "exit":
            # Asumsi exit tidak perlu login
            exit()
        else:
            if hasLogin:
                if command == "register":
                    if isAdmin:
                        register()
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "tambah_game":
                    if isAdmin:
                        add_game()
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "ubah_game":
                    if isAdmin:
                        update_game()
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "ubah_stok":
                    if isAdmin:
                        update_stok()
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "list_game_toko":
                    list_game_toko()
                elif command == "buy_game":
                    if not isAdmin:
                        id_game = input('Masukkan ID Game: ')
                        history = []
                        hasil = buy_game(role,id_game,user_id,saldo,game,kepemilikan,history)
                        history = hasil[0]
                        saldo = hasil[1]
                    else:    
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "my_game":
                    if not isAdmin:
                        inventory()
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "search_my_game":
                    if not isAdmin:
                        search_my_game(role,user_id,kepemilikan,game)
                    else:
                        print("Maaf, Anda tidak memiliki akses pada menu ini")
                        print()
                elif command == "search_game_at_store":
                    search()
                elif command == "topup":
                    if isAdmin:
                        topup()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif command == "history":
                    if not isAdmin:    
                        riwayat()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif command == "help":
                    if isAdmin:
                        help("admin")
                    else:
                        help("user")
                elif command == "save":
                    save()
                elif command == "exit":
                    exit()
                else:
                    # Masukan salah, tidak sesuai keyword yang valid, sudah login
                    print("Input anda tidak valid")
                    print("Berikut merupakan input yang valid")
                    help()        
            elif command in lstPerintah:
                # Masukan benar, tetapi belum login
                print("Anda harus login terlebih dahulu")
                print()
            else:
                # Masukan salah, tidak sesuai keyword yang valid, belum login
                print("Input yang diberikan tidak tersedia")
                print()