# TUGAS COLLECTION

# Isilah dengan beberapa value/nilai, kemudian tampilkan menggunakan perulangan.
# Cobalah update salah satu value/nilai dari Collections tersebut.
# Coba hapus salah satu value dari  Collections.
# Coba tambahkan value ke Collections tersebut.

# TIPE DATA DICTIONARY

novel = {"Judul":"Tentang Kamu","Penulis":"Bang Tere","Penerbit":"Republika","Tahun Terbit":"2016" }

for key in novel:
    print(key,novel[key])

print("="*30)

# MENGUPDATE NILAI
novel["Penulis"] = "Tere Liye"
print(novel)

print("="*30)

# MENGHAPUS NILAI
novel.pop("Tahun Terbit")
print(novel)

print("="*30)

# MENAMBAH NILAI
novel["Jumlah Halaman"] = "524"
print(novel)