print("selamat Datang di Program IPK") 
point= {"A+":4.0, "A":4.0,"A-":3.67,"B+":3.33,"B":3.0,
        "B-":2.67,"C+":2.33,"C":2.0,"D+":1.33,"D":1.0,}
num_courses = 0
total_point=0
done= False
while not done:
    grade=(input("masukkan nilai:"))
    if grade == "":
        done= True
    elif grade not in point:
        print("nilai tidak diketahui '{0}' ".format(grade))
    else:
        num_courses +=1
        total_point+= point[grade]
    if num_courses > 0:
        print(" IPK Anda adalah {0: 3}".format(total_point/num_courses)) 