# Isilah dengan beberapa value/nilai, kemudian tampilkan menggunakan perulangan.
# Cobalah update salah satu value/nilai dari Collections tersebut.
# Coba hapus salah satu value dari  Collections.
# Coba tambahkan value ke Collections tersebut.

print("TUPLE".center(30,"="))

tuple = ("Hendra Usman", 18, 172.5, True)

# PERULANGAN (FOR LOOP)
for i in tuple:
    print(i)
    
print("="*30)

# PERULANGAN (WHILE LOOP)
i = 0
while i < len(tuple):
    print(tuple[i])
    i += 1

# TUPLE BERSIFAT UNCHANGABLE (tidak bisa diubah setelah dideklarasikan)

# MENGAKSES NILAI TUPLE DENGAN INDEKS
jenis_kelamin = ('Pria', 'Wanita', 'Tidak ingin memberitahu')
print(f"Jenis Kelamin : {jenis_kelamin[1]}")
print(f"Jenis Kelamin : {jenis_kelamin[2]}")