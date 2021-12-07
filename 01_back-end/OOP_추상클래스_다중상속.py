from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def print_message(self) -> None:    # None으로 치환되는 type hinting
        pass

    # def... 추상메서드가 아닌 일반메서드는 문제가 생길 수 있다.

class Sendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> None:
        pass

# 추상클래스인 Message와 Sendable을 다중 상속받는다.

class Email(Message, Sendable):
    def __init__(self, content, user_email):
        self.content = content
        self.user_email = user_email

    def print_message(self):
        print("이메일 내용입니다 :\n{}".format(self.content))

    def send(self, destination):
        print("이메일을 주소 {}에서 {}로 보냅니다.".format(self.user_email, destination))


email = Email('안녕하세요. 자소서쓰기싫다.', 'eejj@gmail.com')
print(email.print_message())
print(email.send('sogood@gmail.com'))