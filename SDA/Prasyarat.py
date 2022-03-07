print("Program menghitung gaji karyawan")

nama = input("Masukkan Nama Karyawan:")
gajiPokok = int(input("Masukkan gaji pokok:"))
lamaLembur = int(input("Masukkan lama lembur:"))
gajiLembur = 5000
totalGajiLembur = lamaLembur*gajiLembur
gajiKotor = gajiPokok+totalGajiLembur
pajak = 9/100
potongan = gajiPokok*pajak
gajiBersih = gajiKotor-potongan

print('gaji lembur/jam :', gajiLembur)
print('gaji lembur:', totalGajiLembur)
print('gaji kotor :', gajiKotor)
print('potongan :',potongan)
print('gaji bersih :',gajiBersih)

# Pada program ini yang dikenakan pajak adalah gaji pokok,
# tidak termasuk gaji lembur