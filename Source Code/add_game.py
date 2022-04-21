# Isi array kosong
game = []

def add_game():
    # Menambahkan data game baru ke dalam database
    # I.S. matriks data game terdefinisi
    # F.S. matriks data game ditambahkan data game baru
    
    # KAMUS LOKAL
    # nama_game, kategori, tahun_rilis, harga_game, stok_awal: string
    # valid : boolean
    # add_game, game : array of array of string
    
    # Variable global
    global game

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
            print("Mohon masukkan semua informasi mengenai game agar dapat disimopan di BNMO.")
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
    for i in range(len(game)):
        if game[i][0] == 'GAME'+str(i+1):
            count += 1
    
    # Memberikan ID pada game
    if count <= 9:
        id_game = "GAME00" + str(count+1)
    elif 9 < count <= 99:
        id_game = "GAME0" + str(count+1)
    elif 99 < count <= 999:
        id_game = "GAME" + str(count+1)

    # Menyampaikan pesan sukses dan menambahkan informasi ke dalam database game ketika data sudah valid
    if valid:
        print("Selamat! Berhasil menambahkan game",nama_game+".")
        add_game = [[id_game,nama_game,kategori,tahun_rilis,harga_game,stok_awal]]
        game += add_game

program = True
while program:
    perintah = input(">>> ")
    if perintah == "tambah_game": # Perlu ditambah validasi role (harus "Admin")
        add_game()
    elif perintah == "hasil":
        print(game)
    else:
        program = False