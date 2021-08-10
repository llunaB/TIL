a = [2, 3, 1, 5, 4]

def BubbleSort(a)
    for i in range(len(a)-1, 0, -1) # 4 3 2 1 
        for j in range(0, i): 
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]

