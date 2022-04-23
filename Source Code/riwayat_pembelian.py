def riwayat_pembelian(riwayatgame,user,username):
    index=0
    index2=0
    for i in (user):
        if i[1]==username:
            index=index2
        index2+=1
    j=1
    condition=False
    for i in (riwayatgame):
        if riwayatgame[i][3]==user[index][0]:
            condition=True
            print (f'{j}. {riwayatgame[i][0]} | {riwayatgame[i][1]} | {riwayatgame[i][2]} | {riwayatgame[i][4]}')
            j+=1
    if condition==False:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.')
    
            
            

        
