## for, if 문으로 리스트 간편하게 만들기

nums = [i for i in range(5)]
# [0, 1, 2, 3, 4]

nums2 = [100, 200, 300]
double_nums = [i*2 for i in nums2]
# [200, 400, 600]

nums3 = [i for i in range(10) if i%2 == 0]
# [0, 2, 4, 6, 8]

# 출력 변화 + 조건문 if
nums4 = [100, 300, 500]
double_nums = [i*2 for i in nums if i >= 300]
# [600, 1000]

# 조건문 if 
word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']
word_list_start_a = [i for i in word_list if i[0]=='a']
print(word_list_start_a)
# ['apple', 'apolo', 'abocado']

# None 을 빈 문자열로 변경
word_list2 = ['오메가3', None, '비타500', None, '홍삼절편']

new_word_list2 = []
for i in word_list2:
    if i != None:
        new_word_list2.append(i)
    else:
        new_word_list2.append('')
print(new_word_list2)

# if-else 구문일 경우 for 문 앞에 온다.
new_word_list2 = [i if i != None else '' for i in word_list2]
print(new_word_list2)
# >>> ['오메가3', '', '비타500', '', '홍삼절편']