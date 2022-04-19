# Isi array kosong
user = []

def register_user():
    # Menambahkan data user baru ke dalam database
    # I.S. matriks data user terdefinisi
    # F.S. matriks data user ditambahkan data user baru
    
    # KAMUS LOKAL
    # nama, username, password: string
    # valid : boolean
    # i: integer
    # register, user : array of array of string
    
    # Variable global
    global user 
    
    # ALGORITMA
    # input nama, username, password
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    
    # validasi dari input username
    valid = True
    for i in range(len(username)):
        # validasi karakter yang digunakan dalam username
        if username[i] in ('!@#$%^&*()+={[}]]|\:;<,>.?/'):
            valid = False
            return print("Username",username,"tidak valid, silahkan gunakan username lain.")
    for i in range(len(user)):
        # validasi keunikan username
        if user[i][1] == username:
            valid = False
            return print("Username",username,"sudah terpakai, silahkan gunakan username lain.")

    # Membuat ID user
    count = 0
    for i in range(len(user)):
        if user[i][0][0] == 'U':
            count += 1
    
    id = "User" + str(count+1)

    saldo = 0

    # jika data sudah valid, data akan dimasukkan ke array "user"
    if valid:
        register = [[id,username,nama,password,"User",saldo]]
        user += register
        print("Username",username,"telah berhasil register ke dalam Binomo")

program = True
while program:
    perintah = input(">>> ")
    if perintah == "register":
        register_user()
    elif perintah == "hasil":
        print(user)
    else:
        program = False
