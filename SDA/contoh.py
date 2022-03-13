print("PROGRAM MENGHITUNG GAJI KARYAWAN")

nama = input("Masukkan Nama Karyawan:")
gajiPokok = int(input("Gaji Pokok:"))
lamaLembur = int(input("Masukkan Lama Lembur:"))
gajiLemburPerJam = 5000
totalGajiLembur = lamaLembur*gajiLemburPerJam
gajiKotor = gajiPokok+totalGajiLembur
pajak = 9/100
potongan = gajiPokok*pajak
gajiBersih = gajiKotor-potongan

print("Gaji Lembur/jam :Rp.",gajiLemburPerJam)
print("Total Gaji Lembur :Rp.",totalGajiLembur)
print("Gaji Kotor :Rp.",gajiKotor)
print("Potongan :Rp.",potongan)
print("Gaji Bersih :Rp.",gajiBersih)