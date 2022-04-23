def ubah_game (datagame):
    id_game=input('Masukkan ID game: ')
    index=0
    index2=0
    for i in (datagame):
        if id_game==i[0]:
            index=index2
        index2 += 1       
    nama_game=input('Masukkan nama game: ')
    kategori=input('Masukkan kategori: ')
    tahun_rilis=input('Masukkan tahun rilis: ')
    harga_game=input('Masukkan harga: ')
    if index==0 : 
        print('Maaf game tidak ditemukan')
    else : 
        j=1
        for i in (nama_game,kategori,tahun_rilis,harga_game): 
            if i != '':
                datagame[index][j]=i 
            j+=1



















    
