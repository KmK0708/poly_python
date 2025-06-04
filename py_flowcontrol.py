# if - elif - else문
score = 85

if score >= 90:
    print("A등급")
elif score >= 80:
    print("B등급")
else:
    print("C등급 이하")

# 반복문 for, while
for i in range(5):
    print(i) # 0 1 2 3 4

n = 0
while n < 5:
    print(n)
    n += 1

# 반복 제어문 (break, continue)
for i in range(10):
    if i == 5:
        break
    print(i) # 0 1 2 3 4

for i in range(5):
    if i == 2:
        continue
    print(i) # 0 1 3 4