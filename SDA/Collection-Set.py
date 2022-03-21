# TUGAS COLLECTION

# Isilah dengan beberapa value/nilai, kemudian tampilkan menggunakan perulangan.
# Cobalah update salah satu value/nilai dari Collections tersebut.
# Coba hapus salah satu value dari  Collections.
# Coba tambahkan value ke Collections tersebut.

print("SET".center(30,"="))

set = {"Hendra Usman", 18, 172.5, False}

# PERULANGAN FOR LOOP
for i in set:
    print(i)
    
print("="*30)

# SET TIDAK DAPAT DIUPDATE, KARENA BERSIFAT UNCHANGABLE/INMUTABLE

# MENGHAPUS NILAI/VALUE
# REMOVE
set.remove("Hendra Usman")
print(f"- Set setelah parameter tertentu dihapus : {set} ")

# DISCARD
set.discard(18)
print(f"- Set setelah parameter tertentu dihapus : {set} ")

# CLEAR
set.clear()
print(f"- Set setelah penghapusan : {set} ")

print("="*30)

# MENAMBAHKAN NILAI/VALUE
# ADD
set.add("Endang")
print(f"- Set setelah penambahan nilai : {set} ")

# UPDATE
set.update(["UNSULBAR", "ANGKATAN", 2021])
print(f"- Set setelah penambahan nilai : {set} ")

# SET BERSIFAT UNORDERED (VALUE TIDAK TERURUT DAN TIDAK BISA DIAKSES DENGAN INDEKS