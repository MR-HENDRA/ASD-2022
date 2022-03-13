# OPEARTOR PERBANDINGAN
# <,>,<=,>=,==,!=

x = int(input("Masukkan Angka:"))
y = int(input("Masukkan Angka:"))

operasi1 = x < y
operasi2 = x > y
operasi3 = x <= y
operasi4 = x >= y
operasi5 = x == y
operasi6 = x != y

print("Nilai {} kurang dari {} adalah {}".format(x,y,operasi1))
print("Nilai {} lebih dari {} adalah {}".format(x,y,operasi2))
print("Nilai {} kurang dari atau sama dengan {} adalah {}".format(x,y,operasi3))
print("Nilai {} lebih dari atau sama dengan {} adalah {}".format(x,y,operasi4))
print("Nilai {} sama dengan {} adalah {}".format(x,y,operasi5))
print("Nilai {} tidak sama dengan {} adalah {}".format(x,y,operasi6))