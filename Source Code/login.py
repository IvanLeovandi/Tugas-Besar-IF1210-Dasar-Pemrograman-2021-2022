def login (datauser,x): 
    if x=="login":
        user=input("Masukkan username: ")
        pw=input('Masukkan passsword: ')
        status=False

        for i in (datauser):
            if user==i[1] and pw == i[3]: 
                status=True 
                print(f'Halo {i[2]}! Selamat datang di "Binomo"')
        if status==False :
            status=False 
            print('Password atau username salah atau tidak ditemukan.')
        return status 
    else : 
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')

