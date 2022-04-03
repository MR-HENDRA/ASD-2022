# PROGRAM CRUDS BARANG

# LIST BARANG

('''
1. Gunakan list untuk menampung barang yang diinput

2. Program dapat menambahkan barang 

3. Program dapat menghapus barang

4. Program dapat mengedit barang 

5. Program dapat menampilkan semua barang

6. Program dapat mengetahui apakah barang sudah ada dalam list atau belum

7. Program dapat menampilkan index barang tertentu ''')

tampunganBarang = []

# pembatas
def pembatas():
    print("-"*46)
def pembatas2():
    print("="*46)

# menu
def menu():
    while True :
        pembatas()
        print(" PROGRAM LIST BARANG ".center(46,"="))
        pembatas()
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Edit Barang")
        print("4. Daftar Barang")
        print("5. Cek Barang")
        print("6. Cek Indeks Barang")
        print("7. Keluar")
        
        pembatas()
        
        pilihan = input("Pilih menu \t:").upper()
        if pilihan == "1" or pilihan == "TAMBAH BARANG":
            tambahBarang()
        elif pilihan == "2" or pilihan == "HAPUS BARANG":
            hapusBarang()
        elif pilihan == "3" or pilihan == "EDIT BARANG":
            editBarang()
        elif pilihan == "4" or pilihan == "DAFTAR BARANG":
            daftarBarang()
        elif pilihan == "5" or pilihan == "CEK BARANG":
            cekBarang()
        elif pilihan == "6" or pilihan == "CEK INDEKS BARANG":
            cekIndeks()
        elif pilihan == "7" or pilihan == "KELUAR":
            pembatas()
            print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI".center(46,"="))
            pembatas()
            exit()
        
        else :
            print("Input Salah. Silahkan Masukkan Pilihan Lagi")
        pembatas2()
        
# TAMBAH BARANG
def tambahBarang():
    pembatas()
    print(" PENAMBAHAN BARANG ".center(46,"="))
    pembatas()
    while True :
        barang = input("Masukkan Nama Barang : ")
        tampunganBarang.append(barang)
        print(f'Barang ["{barang}"] Berhasil Ditambahkan')
        pilihan = input("Tambahkan Barang Lagi? (y/n) : ").lower()
        if pilihan == 'y' :
            pembatas()
            print(" DAFTAR BARANG ".center(46,"="))
            pembatas()
            print("Kode".center(18, ' '), "Nama Barang".center(30, ' '), "\n")
            for i in tampunganBarang :
                print("|      ",(tampunganBarang.index(i)+1) ,"          |", (i).center(22, ' '),"|")
            pembatas2()       
        else : 
            menu()

# Next Hapus Barang         
def next():
    lanjut = input('''"Tekan y Jika Ingin Melanjutkan Program, 
    atau Tekan n Untuk Kembali ke Menu" : ''').lower()
    if lanjut == "y" :
            hapusBarang()
    elif lanjut == "n" :
            print('"Program Kembali ke Menu"')
            menu()   
    else :
            print('"Input Salah. Program Kembali ke Menu"')
            menu()
            
# HAPUS BARANG
def hapusBarang():
    pembatas()
    print(" PENGHAPUSAN BARANG ".center(46,"="))
    pembatas()    
    while True :
        hapus = input("Masukkan Nama Barang Yang Ingin Dihapus : ")
        if hapus in tampunganBarang :
            tampunganBarang.remove(hapus)
            print(f'Barang ["{hapus}"] Berhasil Dihapus')
            next()   
        else :
            print(f'Barang ["{hapus}"] Tidak Tersedia')
            next()

# Next Edit Barang         
def next2():
    lanjut2 = input('''"Tekan y Jika Ingin Melanjutkan Program, 
    atau Tekan n Untuk Kembali ke Menu" : ''').lower()
    if lanjut2 == "y" :
            editBarang()
    elif lanjut2 == "n" :
            print('"Program Kembali ke Menu"')
            menu()   
    else :
            print('"Input Salah. Program Kembali ke Menu"')
            menu()
            
# EDIT BARANG :
def editBarang() :
    pembatas()
    print(" DAFTAR BARANG ".center(46,"="))
    pembatas()
    for i in tampunganBarang :
        print("|      ",(tampunganBarang.index(i)+1) ,"          |", (i).center(22, ' '),"|")
    while True :
        pembatas()
        print(" PENGEDITAN BARANG ".center(46,"="))
        pembatas()
        cariBarang = str(input("Masukkan Nama Barang Yang Mau Diedit : "))
        if cariBarang in tampunganBarang :
            ubahKe = input("Ubah Menjadi : ")
            tampunganBarang[tampunganBarang.index(cariBarang)] = ubahKe
            for i in tampunganBarang :
                print("| Kode ".center(18," "),(tampunganBarang.index(i)+1) ,"|", (i).center(22, ' '),"|")
            pembatas()
            print(f'Barang ["{cariBarang}"] Berhasil Diubah Menjadi ["{ubahKe}"]')
            pembatas2()
            next2()
        else :
            print(f'Barang ["{cariBarang}"] Tidak Tersedia')
            pembatas2()
            pass
            next2()
            
# DAFTAR BARANG
def daftarBarang():
    pembatas()
    print(" DAFTAR BARANG ".center(46,"="))
    pembatas()
    print("Kode".center(18, ' '), "Nama Barang".center(30, ' '), "\n")
    for i in tampunganBarang :
            print("|      ",(tampunganBarang.index(i)+1) ,"          |", (i).center(22, ' '),"|")
    pembatas2()  
    exit = input('Enter Untuk Keluar : ')
    if exit == ' ':
        menu()
    else :
        menu()
        
# CEK BARANG
def cekBarang():
    while True :
        print('MENU CEK BARANG'.center(46,'='))
        cek = input("Cek Nama Barang  : ")
        if cek in tampunganBarang :
            print(f'Barang ["{cek}"] Tersedia!')
        else :
            print(f'Barang ["{cek}"] Tidak Tersedia!')
        lanjut = input('Cek Lagi? (y/n) :').lower()
        if lanjut == 'y' :
            pass
        else :
            menu()

# CEK INDEX
def cekIndeks():
        while True :
            print(" MENU CEK INDEKS BARANG".center(46,'='))
            cek = input("Cek Indeks Barang  : ")
            if cek in tampunganBarang :
                print(f"Barang Berada Pada Indeks : {tampunganBarang.index(cek)}")
            else :
                print(f'Barang ["{cek}"] Tidak Tersedia!')
            lanjut = input('Cek Lagi? (y/n) :').lower()
            if lanjut == 'y' :
                pass
            else :
                menu()
            
menu()