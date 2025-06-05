# 클래스 선언
class Member:

    # 속성 생성
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # 메소드 생성
    def info(self):
        print('저의 이름은 {0}이고, 나이는 {1}, 사는곳은 {2} 입니다'.format(self.name, self.age, self.address))

# Member의 introduce 인스턴스 생성
introduce = Member('주영', 26, '서울 특별시')

# introduce 인스턴스의 info 메소드 호출
introduce.info()

class Member:
    value = []

    def info(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print('저의 이름은 {0}이고, 나이는 {1}, 사는곳은 {2} 입니다'.format(self.name, self.age, self.address))

        Member.value.append(age)
        print('클래스 속성 {}'.format(Member.value))

    def info2(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print('저의 이름은 {0}이고, 나이는 {1}, 사는곳은 {2} 입니다'.format(self.name, self.age, self.address))

        Member.value.append(age)
        print('클래스 속성 {}'.format(Member.value))

introduce = Member()

introduce.info('상준', 36, '울산 광역시')
introduce.info2('juyoung', 26, '서울 특별시')

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("잔액 부족")

    def display(self):
        print(f"{self.owner}님의 잔액은 {self.balance}원입니다.")

bank = BankAccount("김주영", 10000)

# 2. 잔액 조회
bank.display()  # 출력: 김주영님의 잔액은 10000원입니다.

# 3. 입금
bank.deposit(5000)
bank.display()  # 출력: 김주영님의 잔액은 15000원입니다.

# 4. 출금
bank.withdraw(3000)
bank.display()  # 출력: 김주영님의 잔액은 12000원입니다.

# 5. 잔액 부족 상황
bank.withdraw(20000)  # 출력: 잔액 부족
bank.display()  # 출력: 김주영님의 잔액은 12000원입니다.