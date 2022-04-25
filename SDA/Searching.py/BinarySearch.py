def binary(data, value):
    low = 0
    high = len(data)-1
    temp=False
    while low <= high and not temp:
        mid = (low+high)//2
        # membandingkan menemukan ketemu!
        if (data[mid])== value:
            temp = True
            print(f"Data {value} ditemukan pada index ke-{mid}")
        # membuang sisa yang tidak diperlukan
        else:
            #jika value yang dicari lebih kecil dari nilai mid
            if (value < data[mid]):
                high = mid-1
            #jika value yang dicari lebih besar dari nilai mid
            else:
                low =mid+1
            
    return temp       

database=[10,30,40,5,50,65,77,69,94,100,2,54]
print(database)
database.sort()
print(database)
binary(database,10)