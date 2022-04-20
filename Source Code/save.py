def save(user,game,riwayat,kepemilikan):
    import os
    
    current_path = os.getcwd()
    path = input('Masukkan nama folder penyimpanan: ')
    if not os.path.exists(path):
        os.mkdir(path)

    os.chdir(path)

    g = open('game.csv', 'w')
    g.write("id;nama;kategori;tahun_rilis;harga;stok\n")
    for i in range (support.f_len(game)):
        for j in range (5):
            g.write(str(game[i][j]))
            g.write(";")
        g.write(str(game[i][5]))
        g.write("\n")
    g.close()

    u = open('user.csv', 'w')
    u.write("id;username;nama;password;role;saldo\n")
    for i in range (support.f_len(user)):
        for j in range (5):
            u.write(str(user[i][j]))
            u.write(';')
        u.write(str(user[i][5]))
        u.write('\n')
    u.close()
    
    r = open('riwayat.csv', 'w')
    r.write("id;username;nama;password;role;saldo\n")
    for i in range (support.f_len(riwayat)):
        for j in range (4):
            r.write(str(user[i][j]))
            r.write(';')
        r.write(str(user[i][4]))
        r.write('\n')
    r.close()

    k = open('kepemilikan.csv', 'w')
    k.write("game_id;user_id\n")
    for i in range (support.f_len(kepemilikan)):
        for j in range (1):
            k.write(str(kepemilikan[i][j]))
            k.write(';')
        k.write(str(kepemilikan[i][1]))
        k.write('\n')
    k.close()

    os.chdir(current_path)
