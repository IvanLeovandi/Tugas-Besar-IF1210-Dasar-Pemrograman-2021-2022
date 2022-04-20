def save():
    import os
    
    path = input('Masukkan nama folder penyimpanan: ')
    if not os.path.exists(path):
        os.mkdir(path)

    os.chdir(path)

    g = open('game.csv', 'w')
    g.write("id;nama;kategori;tahun_rilis;harga;stok\n")
    for i in range (f_len(game)):
        for j in range (5):
            g.write(str(game[i][j]))
            g.write(";")
        g.write(str(game[i][5]))
        g.write("\n")
    g.close()

    u = open('user.csv', 'w')
    u.write("game_id;nama;harga;user_id;tahun_beli\n")
    for i in range (f_len(user)):
        for j in range (5):
            u.write(str(user[i][j]))
            u.write(';')
        u.write(str(user[i][5]))
        u.write('\n')
    u.close()
    
    r = open('riwayat.csv', 'w')
    r.write("id;username;nama;password;role;saldo\n")
    for i in range (f_len(riwayat)):
        for j in range (4):
            r.write(str(user[i][j]))
            r.write(';')
        r.write(str(user[i][4]))
        r.write('\n')
    r.close()

    k = open('kepemilikan.csv', 'w')
    k.write("game_id;user_id\n")
    for i in range (f_len(kepemilikan)):
        for j in range (2):
            k.write(str(user[i][j]))
            k.write(';')
        k.write(str(user[i][2]))
        k.write('\n')
    k.close()




