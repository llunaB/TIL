OriginalList = [0, 4, 1, 3, 1, 2, 4, 1]
SortedList = [0]*len(OriginalList)
k = len(Counts)
print(SortedList)

def Counting_Sort(OriginalList,SortedList, k):
# OriginalList [] -- 입력 배열(1 to k)
# SortedList [] -- 정렬된 배열
# Counts [] -- 카운트 배열


# 중복없는 세트(집합)에서 숫자 크기만큼 리스트 생성
Counts = [0] * k # [0, 0, 0, 0, 0]

# 입력데이터에서 각 항목의 발생 횟수를 세고, 정수항목들로 직접 인덱스되는
# 카운트리스트 Counts에 저장- Counts[0] = 0의 발생 횟수, Counts[i] = i의 발생 횟수
for i in range (0, len(SortedList)) :
    Counts[OriginalList[i]] += 1 # [1, 3, 1, 1, 2]

# 정렬된 집합에서 각 항목 앞에 위치할 항목의 개수를 반영하기 위해 
# Counts의 원소를 조정
for i in range (1, len(Counts)) :
    Counts[i] += Counts[i-1] # [1, 4, 5, 6, 8] - 해당원소 정렬시 리스트의 몇 번째 위치에 들어가야 하는지 보여줌

# 데이터 마지막 항목부터 원소를 정렬
# 마지막 항목이 1 이므로 Counts[1] 확인, 4 이므로 Temp[3]에 1 삽입
# = Counts[1]을 감소시키고 TEMP에 1을 삽입
# 마지막에서 두번째 항목이 4이므로 Counts[4] 확인, 8이므로 Temp[7]에 4 삽입
# Counts[4]를 감소시키고 TEMP에 4를 삽입
# 마지막에서 세번째 항목 (OriginalList[5])이 2이므로 Counts[3] 확인, 5이므로
# Temp[4]에 2를 삽입
for I in range (len(SortedList)-1, -1, -1) :
    SortedList[Counts[OriginalList[i]]-1] = OriginalList[i]
    Counts[OriginalList[i]] -= -1

# [0, 1, 1, 1, 2, 3, 4, 5]