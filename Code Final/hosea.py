import f_len ; import f_append
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
    for i in range(f_len.f_len(username)):
        # validasi karakter yang digunakan dalam username
        if not((ord(username[i]) >= 97 and ord(username[i]) <= 122) or (ord(username[i])>=65 and ord(username[i])<=90) or (ord(username[i])==45) or (ord(username[i])==95) or (ord(username[i])>=48 and ord(username[i])<=57)):
            valid = False
            print("Username",username,"tidak valid, silahkan gunakan username lain.")
    for i in range(f_len.f_len(user)):
        # validasi keunikan username
        if user[i][1] == username:
            valid = False
            print("Username",username,"sudah terpakai, silahkan gunakan username lain.")

    # jika data sudah valid, data akan dimasukkan ke array "user"
    if valid:
        count = 0
        for i in range(f_len.f_len(user)):
            if user[i][0][0] == "U":
                count += 1
        id = "User" + str(count+1)
        saldo = "0"
        register = [id,username,nama,password,"User",saldo]
        user = f_append.f_append(user,register)
        print("Username",username,"telah berhasil register ke dalam Binomo")
    return user

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
    if (f_len.f_len(game)) != 0:
        for i in range(f_len.f_len(game)):
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
        game = f_append.f_append(game,add_game)
        return game

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

    for i in range(f_len.f_len(user)):
        user[i][5] = int(user[i][5])
    # Mencari username yang telah diinput di data base
    found = False
    for i in range(f_len.f_len(user)):
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