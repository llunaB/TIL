import sys
sys.stdin = open("input.txt")

N = int(input()) # number of switches
switches = list(map(int, input().split())) # switch status
stu_num = int(input()) # number of students
stu_info = [list(map(int, input().split())) for _ in range(stu_num)]

# print(N)
# print(switches)
# print(stu_num)
# print(stu_info)

# 8
# [0, 1, 0, 1, 0, 0, 0, 1]
#  0  1  2  3  4  5  6  7  - index
#  1  2  3  4  5  6  7  8  - switch
# 2
# [[1, 3], [2, 3]]

def changeStatus(s):
    if s == 0:
        return 1
    if s == 1:
        return 0

cnt = 0
while cnt < stu_num:
    for i in range(stu_num):
        # if male
        if stu_info[i][0] == 1:
            for j in range(1, N+1): # 1~8
                if j % stu_info[i][1] == 0:
                    switches[j-1] = changeStatus(switches[j-1])

        # if female
        if stu_info[i][0] == 2:
            # if left and right num of received num is same => extend changing range until left != right and change all switches
            if switches[stu_info[i][1] - 1] == switches[stu_info[i][1] - 1]:
                k = 1
                while switches[stu_info[i][1]-1-k] == switches[stu_info[i][1]-1+k] and (stu_info[i][1] - 1 - k >= 0) and (stu_info[i][1] - 1 + k <N):
                    if 0 <= stu_info[i][1] - 1 - k < N and 0 <= stu_info[i][1] - 1 + k < N:
                        k += 1
                        print("k is {}".format(k))
                for s in range(2*(k-1)+1): # 0 1 2 3 4
                    switches[stu_info[i][1]-1+(k-1)-s] = changeStatus(switches[stu_info[i][1]-1+(k-1)-s])
            # if left and right num of received num is not same => change status of received num
        cnt += 1
print(switches)