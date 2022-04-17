data1=[13,6,25,10,47,19,81,4,52,18,67,45,32]

def selectionSort(data):
    print(f"Data Awal : {data}\n")
    langkah=0
    for i in range (len(data)-1,0,-1):
        print(f"langkah ke-{langkah}")
        m=0
        for j in range(1,i+1):
            if data[j] > data[m]:
                m=j
        temp = data[i]
        data[i] = data[m]
        data[m] = temp
        
        langkah+=1
        print(data)
        
selectionSort(data1) 

