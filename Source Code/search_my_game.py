# F10 - Mencari game yang dimiliki
def search_my_game(role, user_id,kepemilikan):
    if role == "User":
        game_id = input("Masukkan ID Game: ")
        tahun_rilis = input("Masukkan Tahun Rilis Game: ")
        for line in kepemilikan:
            pass