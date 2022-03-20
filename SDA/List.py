# Isilah dengan beberapa value/nilai, kemudian tampilkan menggunakan perulangan.
# Cobalah update salah satu value/nilai dari Collections tersebut.
# Coba hapus salah satu value dari  Collections.
# Coba tambahkan value ke Collections tersebut.

# TIPE DATA LIST
print("LIST".center(30,"="))

list_random = ["Hendra Usman", "Pria", "Pangale", 18, 170.5, True]

# PERULANGAN (FOR LOOP)
for i in list_random:
    print(i)

print("="*30)

# PERULANGAN (WHILE LOOP)
i = 0
while i < len(list_random):
    print(list_random[i])
    i += 1

print("="*30)

# MENGUPDATE NILAI
list_random [4] = 172
print(f"- List Random setelah diupdate : {list_random}")

print("="*30)

# MENGHAPUS NILAI 

# POP
value_yang_terhapus = list_random.pop()

print(F"- Value yang terhapus : {value_yang_terhapus}")
print(f"- List Random (setelah value terakhir dihapus) : {list_random}")

# REMOVE
list_random.remove('Pria')

print(f"- List Random (setelah parameter tertentu dihapus) : {list_random}")

# DEL
del list_random[1]
print(f"- List Random (setelah index tertentu dihapus) : {list_random}")

print("="*30)

# MENAMBAHKAN NILAI

# APPEND
list_random.append('Mamuju Tengah')
print(f"- Menambah Data di belakang list : {list_random}")

# EXTEND
list_random.extend([2021])
print(f"- Menambah Data dengan Extend : {list_random}")

# INSERT
list_random.insert(4, 'UNSULBAR')
print(f"- Menambah Data dengan Insert: {list_random}")
