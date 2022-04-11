"""
파이썬 코딩의 기술
책 내용을 참고했습니다.
"""

# 1. 딕셔너리에서 키와 콜론(:) 사이에는 공백을 넣지 않고, 한 줄 안에 키와 값을 같이 넣는 경우 콜론 다음에 스페이스를 넣는다.
my_dict = {
    'key1': 1,
    'key2': 2,
}

# 2. 타입 표기를 덧붙이는 경우에는 변수 이름과 콜론 사이에는 공백을 넣지 말고, 콜론과 타입 정보 사이에는 스페이스를 하나 넣어라


def my_function(var1: str):
    print(var1)

# 3. 함수/변수/특성은 소문자와 밑줄 사용. 클래스는 여러 단어를 붙이고 각 단어의 첫 글자는 대문자로


class MyClass:

    def __init__(self, first_variable):
        self.first_variable = first_variable

    def my_func1(self):
        print(self.first_variable)


# 4. if not a is b와 같은 표현보다는 if a is not b와 같은 표현을 사용하라

a = 2
b = 3

if not (a == b):
    print('a')
else:
    print('b')

if a != b:
    print('a')
else:
    print('b')

# 5. 빈 컨테이너나 시퀀스를 검사할 때 길이 비교를 하지말고 'if not 컨테이너'라는 조건문을 사용해라

a = []
b = [1]

if not a:
    print('list ia empty')
else:
    print(a)

if not b:
    print('list ia empty')
else:
    print(b)

# 6. 모듈을 임포트 하는 경우 무조건 절대 경로를 사용하라. 상대 경로를 사용하는 경우도 명시적인 구문을 사용하라.
from . import something

# 7. 여러 줄에 걸쳐 식을 쓸 떄는 \가 아니라 괄호를 사용하라.