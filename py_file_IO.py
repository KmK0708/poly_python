# 파일 열기: open()
# f = open("파일명", "모드")

# read(): 전체 내용 읽기
f = open("sample.txt", "r", encoding="utf-8")
data = f.read()
print(data)
f.close()

# readline(): 한 줄씩 읽기
f = open("sample.txt", "r", encoding="utf-8")
line = f.readline()
while line:
    print(line.strip())  # 줄바꿈 제거
    line = f.readline()
f.close()

# readlines(): 모든 줄을 리스트로 읽기
f = open("sample.txt", "r", encoding="utf-8")
lines = f.readlines()
for line in lines:
    print(line.strip())
f.close()

# 파일 쓰기 : write(): 문자열을 파일에 쓰기
f = open("output.txt", "w", encoding="utf-8")
f.write("첫 번째 줄입니다.\n")
f.write("두 번째 줄입니다.\n")
f.close()

# with문으로 파일 자동 닫기
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("세 번째 줄입니다.\n")