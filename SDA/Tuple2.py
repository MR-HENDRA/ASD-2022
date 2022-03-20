# TIPE DATA TUPLE
print("TUPLE".center(120,"="))

# Cara Standar dan palng dasar
jenis_kelamin = ('Pria', 'Wanita')
print(jenis_kelamin)

# Tanpa kurung, hal ini normal  dalam python
status_perkawinan = 'Menikah', 'Lajang'
print(status_perkawinan)

# Menggunakan fungsi tuple dan melemparkan list sebagai parameternya
status_kelulusan = tuple(['Lulus', 'Tidak Lulus'])
print(status_kelulusan)

# Tuple dengan satu value
tuple_tunggal = (10,)
print(tuple_tunggal)

# Type Tuple
angka1 = (15,)
angka2 = (15)
print(f"Angka 1 : {angka1} Tipe Data : {type(angka1)}")# yang ini dinggap tuple

# Cara Mengakses nilai tuple
# Cara Standar 
jenis_kelamin = ('Pria', 'Wanita') # bisa juga diakses dengan negatif indeks
print(f"Jenis Kelamin : {jenis_kelamin[1]}")
print(f"Jenis Kelamin : {jenis_kelamin[0]}")

# Slicing Tuple
list_buah = ('Rambutan', 'Nangka', 'Melon', 'Kelapa')
print(f"List Buah : {list_buah}")
print(f"List Buah Setelah di Slicing: {list_buah[0:1]}")
print(f"List Buah Setelah di Slicing: {list_buah[-3:-1]}")

# Sllicing tanpa batas
list_buah = ('Rambutan', 'Nangka', 'Melon', 'Kelapa')
print(f"List Buah : {list_buah}")
print(f"List Buah Setelah di Slicing: {list_buah[1:]}")
print(f"List Buah Setelah di Slicing: {list_buah[:2]}")

# DATA DI TUPLE TIDAK DAPAT DIUBAH !

# Sequence Unpacking
mahasiswa = ('Hendra Usman', 'Mamuju Tengah', 18)
nama, asal, usia = mahasiswa
print('Nama:', nama) # mahasiswa[0]
print('Asal:', asal) # mahasiswa[1]
print('Usia:', usia) # mahasiswa[2]

# Menggabungkan dua buah tuple atau lebih
angka123 = (1, 2, 3)
angka_besar = (40, 50, 60)
tuple_angka = angka123 + angka_besar
print(f"Gabungan Angka: {tuple_angka}")

# fungsi-fungsi bawaan tuple
nilai_semester_2 = (90, 95, 94, 98, 100, 96, 99)
print(f"Nilai Semester 2: {nilai_semester_2}")
print(max(nilai_semester_2))
print(min(nilai_semester_2))
print(len(nilai_semester_2))