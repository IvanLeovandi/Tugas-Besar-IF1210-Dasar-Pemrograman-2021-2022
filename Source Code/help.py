def help():
    # Fungsi menampilkan perintah-perintah yang dapat digunakan pada aplikasi
    print("""
    ============ HELP ============
    1. register - Untuk melakukan registrasi user baru
    2. login - Untuk login ke dalam sistem
    3. tambah_game - Untuk menambah game yang dijual pada toko
    4. ubah_game - Untuk mengubah informasi game pada toko
    5. ubah_stok - Untuk mengubah stok game pada toko
    6. list_game_toko - Untuk menampilkan list game pada toko berdasarkan tahun atau harga
    7. buy_game - Untuk membeli game yang tersedia di toko
    8. my_game - Untuk menampilkan daftar game yang dimiliki pengguna
    9. search_my_game - Untuk mencari game yang dimiliki dari ID dan tahun rilis
    10. search_game_at_store - Untuk mencari game di toko dari ID, nama game, harga, kategori, dan tahun rilis
    11. topup - Untuk menambahkan saldo pada pengguna
    12. history - Untuk menampilkan riwayat pembelian game
    13. help - Untuk menampilkan perintah-perintah yang dapat digunakan pada aplikasi
    14. save - Untuk menyimpan perubahan-perubahan yang telah dilakukan
    15. exit - Untuk keluar dari aplikasi
    """)

program = True
while program:
    perintah = input(">>> ")
    if perintah == "help":
        help()
    else:
        program = False
