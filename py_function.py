# 함수 간단한 예제
def say_hello():
    print("안녕하세요!")

say_hello()  # 함수 호출

# 매개변수가 있는 함수
def greet(name):
    print(f"{name}님, 안녕하세요!")

greet("주영")  # 출력: 주영님, 안녕하세요!

# 리턴 값을 사용하는 함수
def add(a, b):
    return a + b

result = add(3, 5)

print(result)  # 출력: 8

# 기본값 매개변수
def greet(name="OO"):
    print(f"{name}님, 안녕하세요!")

greet()        # OO님, 안녕하세요!
greet("지수")  # 지수님, 안녕하세요!

# *args: 여러 개의 위치 인자 받기 (튜플로 처리됨)
def greet(*names):
	"""이 함수 이름 튜플에 있는 모든 사람을
	인사합니다.."""
	
	# names is a tuple with arguments
	for name in names:
		print("Hello", name)
	
greet("Monica", "Luke", "Steve", "John")

# 람다 함수
square = lambda x: x * x
print(square(3))  # 출력: 9