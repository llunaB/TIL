import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    words = list(input().split())

    result = []
    mid = len(words) // 2
    left = words[:mid]  # ['A', 'B', 'C']
    right = words[mid:] # ['D', 'E', 'F']

    # words의 길이가 홀수일 때
    if len(words) % 2:
        left = words[:mid+1]
        right= words[mid+1:]

    for i in range(len(right)): # 오른쪽 배열의 길이를 기준으로
        result.append(left[i])
        result.append(right[i])

    # 만약 전체 길이가 홀수라면
    if len(words) % 2:
        result.append(left[-1])

    print("#{} {}".format(tc, ' '.join(result)))