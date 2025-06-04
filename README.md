# poly_python
<h1 align="center">
  
## 🗂 문서 개요
이 저장소는 Python 학습 정리 레포지토리입니다. 각 문단 별로 학습한 내용을 정리두었으며, 예제도 일부 포함되어 있습니다.

### ✅ 주요 학습 주제 예시

- 파이썬 기본 문법 (변수, 자료형, 연산자)
- 제어문 (조건문, 반복문)
- 함수 정의 및 활용
- 자료구조 (리스트, 튜플, 딕셔너리, 집합)
- 파일 입출력
- 클래스 정의 및 활용

<details>
  <summary><strong>📌 변수 (Variables)</strong></summary>
  <!-- 내용 -->
  파이썬에서 변수는 데이터를 저장하기 위한 이름표로, 값을 메모리에 저장하고 나중에 참조할 수 있게 해줍니다.</br>
  
  ## Python variables(변수)

- 메모리에 데이터를 저장하기 위해 사용되는 지정된 위치

➡️number = 10 : 변수를 number라는 이름으로 선언

➡️number = 1.1 : 변수의 내용물은 언제든 변경 가능

- 변수에 데이터/값을 할당하기 위해선 =(대입 연산자) 기호 사용

➡️ 파이썬은 type-inferred 언어로 변수 유형을 명시적으로 정의할 필요 없음

❗숫자는 그냥 사용 가능하지만 문자는 따옴표 ( “ “, ‘ ‘ )사용 해야 함.

  ## 변수 타입
  정수 (int): 소수점이 없는 숫자

  실수 (float): 소수점이 있는 숫자

  문자열 (str): 텍스트 데이터

  불리언 (bool): 참/거짓 값
</details>

<details>
  <summary><strong>📌 <a href="https://gold-century-3b0.notion.site/12-Python-03-19-3-1bb3bfade93280efb762f3664b616430">연산자</a> (Operator)</strong></summary>
  <!-- 내용 -->
  연산자(Operators)는 값을 계산하거나 비교하거나 조합할 때 사용하는 기호</br>
  
  1. 산술 연산자 (Arithmetic Operators)

+ : 덧셈
- : 뺄셈
* : 곱셈
/ : 나눗셈 (실수 결과)
// : 몫 (정수 나눗셈)
% : 나머지
** : 거듭제곱

2. 비교 연산자 (Comparison Operators)

== : 같음
!= : 다름
> : 초과
< : 미만
>= : 이상
<= : 이하

3. 논리 연산자 (Logical Operators)

and : 논리곱 (그리고)
or : 논리합 (또는)
not : 논리부정 (아니다)

4. 대입 연산자 (Assignment Operators)

= : 기본 대입
+=, -=, *=, /= : 복합 대입
//=, %=, **= : 복합 대입

5. 멤버십 연산자 (Membership Operators)

in : 포함됨
not in : 포함되지 않음

6. 식별 연산자 (Identity Operators)

is : 동일한 객체
is not : 다른 객체

7. 비트 연산자 (Bitwise Operators)

& : 비트 AND
| : 비트 OR
^ : 비트 XOR
~ : 비트 NOT
<< : 왼쪽 시프트
>> : 오른쪽 시프트
</details>

<details>
  <summary><strong>📌 <a href="https://gold-century-3b0.notion.site/18-python-03-27-4-1c03bfade9328060beded0f5f7cb137e">흐름제어</a> (Flow Control)</strong></summary> 
  <!-- 내용 -->
  파이썬 흐름 제어란, 프로그램의 실행 순서를 특정 조건이나 반복문을 통해 동적으로 변경하는 것을 의미합니다. 
  
  즉, 코드가 순서대로 실행되지 않고, 특정 조건이 만족되었거나 반복문을 통해 실행이 반복되는 과정을 제어하는 것입니다.</br>
  
  ## 조건문 (Conditional Statements)
  if문

  조건이 참일 때 실행</br></br>
  if 조건:
  
  if-else문
  
  조건이 참이면 if 블록, 거짓이면 else 블록 실행</br></br>
  if 조건: ~ else:
  
  if-elif-else문
  
  여러 조건을 순차적으로 검사</br></br>
  if 조건1: ~ elif 조건2: ~ else:

  ## 반복문 (Loop Statements)
  for문 :

  정해진 횟수만큼 반복</br></br>
  시퀀스(리스트, 문자열 등)의 각 요소에 대해 반복</br></br>
  for 변수 in 시퀀스:
  
  while문: 
  
  조건이 참인 동안 계속 반복</br></br>
  while 조건:

  ## 반복제어문 (Loop Control)

  break

  반복문을 즉시 종료하고 빠져나감
  
  continue
  
  현재 반복을 건너뛰고 다음 반복으로 이동
  
  pass
  
  아무것도 하지 않음 (문법적으로 문장이 필요할 때 사용)
</details>

<details>
  <summary><strong>📌 <a href="https://gold-century-3b0.notion.site/18-python-03-27-4-1c03bfade9328060beded0f5f7cb137e">함수</a> (Function)</strong></summary>
  <!-- 내용 -->
  함수(Function)는 특정 작업을 수행하는 코드 블록(명령문(statement)의 그룹)

  **함수는 코드의 재사용성**을 높이고, 가독성을 개선하며, **유지보수**를 쉽게 만들어 준다..</br>
  
  ## 함수 예시

  def 함수이름(매개변수1, 매개변수2, ...):
  
    실행할 코드
    return 반환값  # 반환값은 선택 사항

  ⚠️ **사용 전 선언되어 있어야 함**

  - 리턴 명령문 사용 가능
  - 변수의 적용 범위는 함수 내부, 외부가 별개임
  - 사용자가 정의한 함수와 파이썬 자체 함수가 존재
    
</details>

<details>
  <summary><strong>📌 <a href="https://gold-century-3b0.notion.site/28-04-10-6-1d13bfade93280ccaf92d137305db5fd">파일 입출력</a></strong></summary>
  <!-- 내용 -->
  파이썬에서의 **File I/O (Input/Output)**는 **파일을 열고, 읽고, 쓰고, 닫는 과정**을 의미

  즉, 텍스트 파일이나 데이터 파일을 프로그램에서 사용할 수 있도록 읽거나, 결과를 파일에 저장할 수 있게 만드는 기능</br>
  
 
</details>

## 🛠️ 개발 환경

- **Tool**: Google Colab, VSCode
