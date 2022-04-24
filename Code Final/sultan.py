import f_len ; import f_append ; import f_max_length ; import argparse ; import time ; import f_open ; import sys ; import os
# F03 - Login
def login (user):
    # fungsi yang digunakan pengguna untuk masuk ke dalam sistem

    # KAMUS LOKAL
    # username, pw, user_id, role, saldo = data_user
    # status = boolean
    # i = integer

    # ALGORITMA
    username = input("Masukkan username: ")
    pw = input('Masukkan passsword: ')
    status=False
    user_id = ""
    role = ""
    saldo = "0"
    for i in (user):
        if username == i[1] and pw == i[3]: 
            status=True 
            print(f'Halo {i[2]}! Selamat datang di "Binomo"')
            user_id = i[0]
            role = i[4]
            saldo = i[5]
            return user_id,username,role,saldo,status
    if status == False:
        print('Password atau username salah atau tidak ditemukan.')
        return user_id,username,role,saldo,status

# F05 - Mengubah Game
def ubah_game (game):
    # prosedur untuk mengganti informasi game pada toko

    # KAMUS LOKAL
    # id_game, nama_game, kategori, tahun_rilis, harga_game = data_game
    # index, index2, i, j = integer

    # ALGORITMA
    id_game=input('Masukkan ID game: ')
    index=-1
    index2=0
    for i in (game):
        if id_game==i[0]:
            index=index2
        index2 += 1       
    nama_game=input('Masukkan nama game: ')
    kategori=input('Masukkan kategori: ')
    tahun_rilis=input('Masukkan tahun rilis: ')
    harga_game=input('Masukkan harga: ')

    if game == []:
        print("Data game pada toko kosong, silahkan minta Admin untuk menambahkan Game pada toko.")
    elif index == -1:
        print("Maaf, game tidak ditemukan.")
    else:
        j=1
        for i in (nama_game,kategori,tahun_rilis,harga_game): 
            if i != '':
                game[index][j]=i 
            j+=1

# F13 - Melihat riwayat pembelian
def riwayat_pembelian(riwayatgame,user,username):
    # prosedur yang digunakan user untuk melihat riwayat pembelian game
    
    # KAMUS LOKAL
    # index, index2, arr_length_max, max_length, length_data: integer
    # condition: boolean
    # show_riwayat: array of data_history

    # ALGORITMA
    show_riwayat=[]
    index=0
    index2=0
    for i in (user):
        if i[1]==username:
            index=index2
        index2+=1

    condition=False
    for i in range(f_len.f_len(riwayatgame)):
        if riwayatgame[i][3]==user[index][0]:
            condition=True
            show_riwayat = f_append.f_append(show_riwayat,[riwayatgame[i][0],riwayatgame[i][1],riwayatgame[i][2],riwayatgame[i][4]])

    # menampilkan output
    if condition==False:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah buy_game untuk membeli.')
    else:
        print("Daftar game:")
        arr_length_max = f_max_length.max_length(show_riwayat)
        for i in range(f_len.f_len(show_riwayat)):
            if (i < 9):
                print(i+1, end=".   ")
            elif(9 <= i < 99):
                print(i+1, end=".  ")
            else:
                print(i+1, end=". ")
            for j in range(f_len.f_len(show_riwayat[0])):
                max_length = arr_length_max[j]
                length_data = f_len.f_len(show_riwayat[i][j])
                if(j == f_len.f_len(show_riwayat[0])-1):
                    print(show_riwayat[i][j])
                else:
                    print(str(show_riwayat[i][j]) + " "*(max_length-length_data),end = " | ")

# F15 - Load
def load (loaded):
    # fungsi yang digunakan untuk memuat file pada database
    
    # KAMUS LOKAL
    # game = array of data_game
    # user = array of data_user
    # riwayat = array of history
    # kepemilikan = array of data_kepemilikan
    # loaded = bool

    # ALGORITMA
    print('Loading...')
    time.sleep(2)
    if len(sys.argv)!=1:
        parser=argparse.ArgumentParser(usage="")
        parser.add_argument("x")
        args=parser.parse_args()
        namafolder=args.x
        if (os.path.exists(args.x)): 
            game=f_open.f_open(f"{namafolder}/game.csv")
            user=f_open.f_open(f"{namafolder}/user.csv")
            riwayat=f_open.f_open(f"{namafolder}/riwayat.csv")
            kepemilikan=f_open.f_open(f"{namafolder}/kepemilikan.csv")
            loaded = True
            return (loaded,game,user,riwayat,kepemilikan) 
        else : 
            print (f"folder {args.x} tidak ditemukan")
            loaded = False
            return (loaded,[],[],[],[]) 
    else:
        print ("Tidak ada nama folder yang diberikan!")
        loaded = False
        return (loaded,[],[],[],[]) 