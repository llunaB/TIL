import sys
sys.stdin = open('input.txt')

array = list(map(int,input()))
for i in range(len(array)//7):
    binary = array[i*7+1:i*7+8]
    s = binary[::-1] 
    ten = 0
    for i in range(len(s)): 
        if i == 0:
            x = 1 if s[i] == 1 else 0
            ten += x          
        else:
            if s[i] == 1:
                ten = ten + (2 ** i)           
    print(ten)