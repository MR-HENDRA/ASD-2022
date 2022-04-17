# Bubble Sort

database=[21,34,56,78,90,12,45,67,89,11,33]
print(f"Sebelum diurutkan : {database}\n")
print(f"Banyak data : {len(database)}\n")

def bubbleSortAsc(data): # ASCENDING 
    for i in range(len(data)-1,0,-1):
        print("langkah")
        for j in range(0, len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        print(data)
        
bubbleSortAsc(database)

database=[21,34,56,78,90,12,45,67,89,11,33]
print(f"Sebelum diurutkan : {database}\n")
print(f"Banyak data : {len(database)}\n")

def bubbleSortDesc(data): # DESCENDING
    for i in range(len(data)-1,0,-1):
        print("langkah")
        for j in range(0, len(data)-1):
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        print(data)
        
bubbleSortDesc(database)