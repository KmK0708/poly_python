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
  <summary><strong>📌 연산자 (Operator)</strong></summary>
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

## 🛠️ 개발 환경

- **Tool**: Google Colab, VSCode
