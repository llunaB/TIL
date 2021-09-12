# import socket

# # 닉네임을 사용자에 맞게 변경해 주세요.
# NICKNAME = 'SEOUL01_PYTHON'

# # 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
# HOST = '127.0.0.1'

# # 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
# PORT = 1447
# CODE_SEND = 9901

# class Conn:
#     def __init__(self):
#         self.sock = socket.socket()
#         print('Trying to Connect: %s:%d' % (HOST, PORT))
#         self.sock.connect((HOST, PORT))
#         print('Connected: %s:%d' % (HOST, PORT))
#         send_data = '%d/%s' % (CODE_SEND, NICKNAME)
#         self.sock.send(send_data.encode('utf-8'))
#         print('Ready to play!\n--------------------')

#     def close(self):
#         self.sock.close()
#         print('Connection Closed.\n--------------------')


# def main():
#     conn = Conn()
#     conn.close()


# if __name__ == '__main__':
#     main()

import math
# angle
# strenth

balls = [[10, 10], [50, 40]]
a1, b1 = balls[0][0], balls[0][1]
a2, b2 = balls[1][0], balls[1][1]

# 두 점 사이의 거리 계산
width = abs(a2 - a1)
height = abs(b2 - b1)
distance = (width ** 2 + height ** 2) ** 0.5

# 두 점 사이의 각도 계산
# 아크탄젠트로 라디안 값을 구하고 이를 다시 각도로 변환
degree = math.degrees(math.atan(height/width))
print(degree)
print(a1, b1, a2, b2, distance)