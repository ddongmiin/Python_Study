class Solution(object):
    def reverse(self, x):
        if x < 0 :
            x = "-" + str(x)[-1::-1][:-1]
        else : 
            x = str(x)[-1::-1]

        x_int = int(x)

        if x_int >= (-2)**31 and x_int <= (2**31 -1):
            return x_int
        else:
            return 0

inst1 = Solution()
print(inst1.reverse(12340000))


