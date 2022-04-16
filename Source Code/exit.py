# F17 - Exit
def exit(hasil):
    answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while (answer != "y" or answer != "Y" or answer != "n" or answer != "N"):
        answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if (answer == "Y" or answer == 'y'):
        # save()
        print("Data berhasil disimpan.")
        print("Anda telah keluar dari program.")
    else:
        print("Data tidak disimpan.")
        print("Anda telah keluar dari program.")
    # close()