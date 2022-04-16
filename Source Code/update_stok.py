# F06 - Mengubah stok game
def update_stok(role,hasil):
    if role == 'Admin':
        id_game = input('Masukkan ID game: ')
        jumlah = int(input('Masukkan jumlah: '))  
         
        for line in hasil:
            if id_game == line[0]:
                if (line[5] + jumlah) >= 0: 
                    line[5] += jumlah
                    print('Stok game', line[1], 'berhasil ditambahkan. Stok sekarang:', line[5])
                    break
                else:
                    print('Stok game', line[1], 'gagal dikurang karena stok kurang. Stok sekarang:', line[5])
                    break
            else:
                print('Tidak ada game dengan ID tersebut')
                break
    else:
        print('Kamu tidak memiliki akses pada menu ini')

# update_stok('admin', hasil)