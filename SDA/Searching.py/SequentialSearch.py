def sequential(database, value):
    start = 0
    temp = False
    while start < len(database) and not temp:
        #membandingkan data yang ada di database dengan value
        if database[start] == value:
            temp = True
            print(f"Data {value} ditemukan pada index ke-{start}")
        else:
            start += 1
    return temp
    
database=[10,50,30,70,80,60,20,90,40]
sequential(database, 80)