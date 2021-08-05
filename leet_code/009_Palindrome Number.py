"""
문제 설명 : 앞에서 읽어도 뒤에서 읽어도 같은 숫자이면 true, 다르면 false

문제 해결 순서
1. 숫자를 받아 string으로 변환 시킨다. 
2. 원래 숫자와 reverse한 숫자(string)가 일치하는지 비교한다.
3. 일치하면 true를 일치하지 않으면 false를 반환한다.
"""

class Solution(object):
    def isPalindrome(self, x: int) :
        
        if x >= (-2)**31 and x <= (2**31 -1):
            str_x = str(x)
            x_reverse = str_x[::-1]

            if str_x == x_reverse :
                return True
            else :
                return False
        
        else :
            return False
