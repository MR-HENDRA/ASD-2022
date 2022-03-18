# TIPE DATA LIST
print("LIST".center(120,"="))

# list yang berisi kumpulan string
list_buah = ['Rambutan', 'Nangka', 'Melon', 'Kelapa'] #1
print(f"- List Buah : {list_buah}") #2

# list yang berisi kumpulan integer
list_nilai = [75, 43, 69, 80]
print(f"- List Nilai : {list_nilai}")

# list campuran berbagai tipe data
list_jawaban = [100, 45.7, 'Hendra', True]
print(f"- List Jawaban : {list_jawaban}")

list_buah = ['Rambutan', 'Nangka', 'Melon', 'Kelapa'] #1
print(f"- List Buah : {list_buah}")

# menampilkan isi tertentu dari list dengan indeks
print(f"- Data Index [0] : {list_buah[0]}")

# menampilkan isi data dari belakang
print(f"- Data Index [-2] : {list_buah[-2]}")

# slicing tanpa batas
print(f"- Data Index [1:] : {list_buah[1:]}") # indeks = 1,2,3

# mengubah data dalam list
list_buah[1] = 'Anggur'
print(f"- Mengubah Data Index [1] : {list_buah}")

# menambah data di belakang list
list_buah.append('Sirsak')
print(f"- Menambah Data di belakang list : {list_buah}")

# menambah data di awal list
list_buah.insert(0, 'Jambu')
print(f"- Menambah Data di awal list : {list_buah}")

# menambah data di index mana pun dalam list
list_buah.insert(2, 'Manggis')
print(f"- Menambah Data di awal list : {list_buah}")

print(f"- List Buah Terbaru : {list_buah}")

# hapus satu buah di belakang
buah_yang_terhapus = list_buah.pop()

print(F"- Buah yang terhapus : {buah_yang_terhapus}")
print(f"- List Buah (setelah buah terakhir dihapus) : {list_buah}")

# Menghapus data yang memiliki nilai yang sama dengan parameter
list_buah.remove('Jambu')

print(f"- List Buah (setelah jambu dihapus) : {list_buah}")

# Menghapus indeks berapa pun dari item list.
list_buah[1]
print(f"- List Buah (setelah index 1 dihapus) : {list_buah}")

# urutkan secara ascending
list_buah.sort()
print(f"- List Buah setelah diurutkan : {list_buah}")

# membalikkan posisi item list (tidak harus berurut)
list_buah.reverse()
print(f"- List Buah setelah nilainya dibalik : {list_buah}")

angka = [1, 2, 3]
string = ['Hendra','Usman']
campuran = [True, 4.25]

listBaru = angka + string + campuran

print(f"- List Baru : {listBaru}")


