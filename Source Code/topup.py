# Isi array diumpamakan
user = [["U1","Hosea","Hosea_N","1234",5000,"User"],["U2","Ivan","Ivan_L","1122",0,"User"]]

def topup():
    # Menambahkan data saldo pada user tertentu
    # I.S. matriks data user terdefinisi
    # F.S. 
    
    # KAMUS LOKAL
    # username : string
    # saldo_tambahan : integer
    # found : Boolean
    # user : array of array of string and integer
    # i : integer
    
    # Variable global
    global user

    # Algoritma
    # Menerima input username dan saldo tambahan
    username = input("Masukkan username: ")
    saldo_tambahan = int(input("Masukkan saldo: "))

    # Validasi saldo tambahan
    if saldo_tambahan < 0:
        print("Masukkan tidak valid.")
    else:
        # Mencari username yang telah diinput di data base
        found = False
        for i in range(len(user)):
            # Jika username ditemukan, akan dilakukan penambahan saldo
            if user[i][2] == username:
                found = True
                user[i][4] += saldo_tambahan
                print("Top up berhasil. Saldo",username,"bertambah menjadi",user[i][4])
                break
        # Jika username tidak ditemukan, akan menyampaikan pesan error
        if found == False:
            print("Username",username,"tidak ditemukan.")
            
        


program = True
while program:
    perintah = input(">>> ")
    if perintah == "topup": # Perlu ditambahkan validasi role (harus Admin)
        topup()
    elif perintah == "hasil":
        print(user)
    else:
        program = False