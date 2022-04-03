# PROGRAM STACK
# TUMPUKAN BARANG

# Pop, peek/top, push, empty, size

stack=[]

# pembatas
def pembatas():
    print("="*46)
    
def menu():
    while True:
        print("\n")
        pembatas()
        print(" PROGRAM STACK BARANG ".center(46,"-"))
        pembatas()
        print("DAFTAR MENU".center(46," "))
        print("1. Daftar Barang")
        print("2. Push")
        print("3. Pop")
        print("4. Peek")
        print("5. Size")
        print("6. Empty")
        print("7. Exit")
        pembatas()
        pilihan = input("Pilih menu:").upper()
        if pilihan == '1' :
            daftarBarang()
        elif pilihan == "2" :
            push()
        elif pilihan == "3" :
            pop()
        elif pilihan == "4" :
            peek()
        elif pilihan == "5" :
            size()
        elif pilihan == "6" :
            empty()
        elif pilihan == "7" :
            pembatas()
            print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI".center(46,"-"))
            pembatas()
            exit()
        else :
            print("Input Salah. Silahkan Masukkan Pilihan Lagi")


def daftarBarang():
    print("\n")
    pembatas()
    print(" DAFTAR BARANG ".center(46,"-"))
    pembatas()
    if len(stack) == 0 :
        print("Stack Kosong !".center(46," "))
    else :
        for i in stack:
            print(i)
    pembatas()
            
def push(): 
    print("\n")
    pembatas()
    print(" PUSH ".center(46,"-"))
    pembatas()
    while True :
            barang = input("Masukkan Nama Barang : ")
            stack.append(barang)
            print(f'Barang ["{barang}"] Berhasil Ditambahkan')
            pembatas()
            daftarBarang()
            pilihan = input("Tambahkan Barang Lagi? (y/n) : ").lower()
            if pilihan == 'y' :
                push()
            elif pilihan == 'n' :
                menu()
            else :
                print("Inputan Salah. Program Kembali ke Menu")
                menu()
            
def pop():
    print("\n")
    pembatas()
    print(" POP ".center(46,"-"))
    pembatas()
    if len(stack) == 0 :
        print("Stack Kosong !".center(46," "))
        pembatas()
    else :
        print(f'Barang ["{stack.pop()}"] Berhasil Dihapus')
        pembatas()
        daftarBarang()
        pilihan = input("Hapus Barang Lagi? (y/n) : ").lower()
        if pilihan == 'y' :
            pop()
        elif pilihan == 'n' :
            menu()
        else :
            print("Inputan Salah. Program Kembali ke Menu")
            menu()
        
def peek():
    print("\n")
    pembatas()
    print(" PEEK ".center(46,"-"))
    pembatas()
    if len(stack) == 0 :
        print("Stack Kosong !".center(46," "))
        pembatas()
    else :
        print(stack[-1], "Adalah Barang Teratas")
        pembatas()
        daftarBarang()
    
    
def size():
    print("\n")
    pembatas()
    print(" SIZE ".center(46,"-"))
    pembatas()
    print(f'Jumlah Barang : {len(stack)}')
    pembatas()

def empty():
    print("\n")
    pembatas()
    print(" EMPTY ".center(46,"-"))
    pembatas()
    if len(stack) == 0 :
        print("Stack Kosong !".center(46," "))
        pembatas()
    else :
        print("Stack Tidak Kosong !".center(46," "))
        print("Barang Yang Ada : ".center(46," "))
        pembatas()
        daftarBarang()
        
menu()
