# Isi array diumpamakan
kepemilikan = [["GAME001","BNMO - Play Along With Crypto","Adventure","2022","100.000"],["GAME069","Python Gemink","Programming","1991","69.000"]]

def inventory():
    # Menampilkan data game yang sudah dimiliki oleh user
    # I.S. matriks data kepemilikan terdefinisi
    # F.S. matriks data kepemilikan dimunculkan pada layar
    
    # KAMUS LOKAL
    # i,j : integer
    
    # Variable global
    global kepemilikan

    # Algoritma
    # jika array kepemilikan tidak ada data, akan ditampilkan pesan error
    if len(kepemilikan) == 0:
        return print("Maaf, kamu belum membeli game. Ketik perintah buy untuk membeli")
    # jika ada data, data akan ditampilkan ke layar
    else:
        print("Daftar game:")
        for i in range(len(kepemilikan)):
            print(str(i+1)+".",end=" ")
            for j in range(5):
                print(kepemilikan[i][j],end=" | ")
            print()

program = True
while program:
    perintah = input(">>> ")
    if perintah == "list_game": # Perlu ditambah validasi role (harus "User")
        inventory()
    else:
        program = False
