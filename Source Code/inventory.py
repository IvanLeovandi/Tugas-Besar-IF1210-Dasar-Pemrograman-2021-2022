# Isi array diumpamakan
game = [["GAME1","BNMO - Play Along With Crypto","Adventure","2022","100.000"],["GAME2","Python Gemink","Programming","1991","69.000"]]
kepemilikan = [["User1","GAME1","GAME2"],["User2","GAME3","GAME4"]]

def inventory(User_ID):
    # Menampilkan data game yang sudah dimiliki oleh user
    # I.S. matriks data kepemilikan dan data gameterdefinisi
    # F.S. matriks data game yang dimiliki dimunculkan pada layar
    
    # KAMUS LOKAL
    # i,j : integer
    
    # Variable global
    global game
    global kepemilikan

    # Algoritma
    # Mencari apakah user ID milik pengguna
    for i in range(len(kepemilikan)):
        if kepemilikan[i][0] == User_ID:
            break

    # Memunculkan game yang dimili dengan user ID yang ditentukan
    count = 0
    for j in range(1,len(kepemilikan[i])):
        for k in range(len(game)):
            if kepemilikan[i][j] == game[k][0]:
                count += 1
                print(str(k+1)+".",end=" ")
                for l in range(5):
                    print(game[k][l],end=" | ")
                print()
    
    # Jika user dengan ID tersebut tidak memiliki game, akan ditampilkan pesan error
    if count == 0:
        return print("Maaf, kamu belum membeli game. Ketik perintah buy untuk membeli")



User_ID = "User1"
program = True
while program:
    perintah = input(">>> ")
    if perintah == "list_game": # Perlu ditambah validasi role (harus "User")
        inventory(User_ID)
    else:
        program = False