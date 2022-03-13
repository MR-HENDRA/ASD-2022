print("IF")
nilai = int(input("Masukkan Nilai:"))
if nilai >= 80:
    print("Nilai A")
print(nilai)

print("IF ELSE")
nilai = int(input("Masukkan Nilai:"))
if nilai >= 60:
    print("Anda Lulus !")
else :
    print("Mohon Maaf, Anda Tidak Lulus !")
    
print("ELIF")
umur = int(input("Masukkan Umur:"))
if umur >= 18 and umur < 30:
    print("Sudah beranjak dewasa")
elif umur >= 30 and umur < 45:
    print("Masa Emas")
elif umur >= 45 and umur < 55:
    print("Masuk Paruh Baya")
elif umur >= 55:
    print("Masa Manula")
else :
    print("Masih dibawah umur")