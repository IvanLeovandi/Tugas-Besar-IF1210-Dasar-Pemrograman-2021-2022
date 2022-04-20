def help(curr_role):
    # Fungsi menampilkan perintah-perintah yang dapat digunakan pada aplikasi jika belum login/belum ada role tertentu
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
    elif curr_role == "admin":
        print("""
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
        11. exit - Untuk keluar dari aplikasi
        """)

    # Fungsi menampilkan perintah-perintah yang dapat digunakan pada aplikasi jika sudah login dan ada role user
    elif curr_role == "user":
        print("""
        1. login - Untuk login ke dalam sistem
        2. list_game_toko - Untuk menampilkan list game pada toko berdasarkan tahun atau harga
        3. buy_game - Untuk membeli game yang tersedia di toko
        4. list_game - Untuk menampilkan daftar game yang dimiliki pengguna
        5. search_my_game - Untuk mencari game yang dimiliki dari ID dan tahun rilis
        6. search_game_at_store - Untuk mencari game di toko dari ID, nama game, harga, kategori, dan tahun rilis
        7. riwayat - Untuk menampilkan riwayat pembelian game
        8. help - Untuk menampilkan perintah-perintah yang dapat digunakan pada aplikasi
        9. save - Untuk menyimpan perubahan-perubahan yang telah dilakukan
        10. exit - Untuk keluar dari aplikasi
        """)


program = True
curr_role = "" # curr_role bisa dibuat pada saat login
while program:
    perintah = input(">>> ")
    if perintah == "help":
        help(curr_role)
    else:
        program = False