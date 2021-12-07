class CheckingAccount:
    """자유 입출금 계좌 클래스"""
    def __init__(self, name, balance, max_spending):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        # self.name = name
        # self.balance = balance
        self.max_spending = max_spending

    # def withdraw(self, amount):
    #     """돈을 출금한다"""
    #     self.balance -= amount

    # def deposit(self, amount):
    #     """돈을 입금한다"""
    #     self.balance += amount

    def use_check_card(self, amount):
        """한 회 사용 한도 초과 이하인 금액을 체크 카드 결제 시 예치금을 줄인다"""
        if amount <= self.max_spending:
            self.balance -= amount
        else:
            print("{}님의 체크 카드는 한 회 {} 초과 사용 불가능합니다".format(self.name, self.max_spending))

    def __str__(self):
        """자유 입출금 계좌의 정보를 문자열로 리턴한다."""
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)


class SavingsAccount:
    """저축 계좌 클래스"""
    def __init__(self, name, balance, interest_rate):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        # self.name = name
        # self.balance = balance
        self.interest_rate = interest_rate

    # def withdraw(self, amount):
    #     """돈을 출금한다"""
    #     self.balance -= amount

    # def deposit(self, amount):
    #     """돈을 입금한다"""
    #     self.balance += amount

    def add_interest(self):
        """이자를 더한다"""
        self.balance *= (1+self.interest_rate)

    def __str__(self):
        """저축 계좌의 정보를 문자열로 리턴한다."""
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)