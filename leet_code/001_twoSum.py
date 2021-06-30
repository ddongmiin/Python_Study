#https://deftkang.tistory.com/167 해당 사이트를 참조 했습니다.


class Solution(object):

    #1.Basic __ Using For Loop
    def twoSum1(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == (nums[i] + nums[j]):
                    return nums[i] + nums[j]

    #2. Using Hash
    def twoSum2(self, nums, target):

        temp_dict = {}

        for i, v in enumerate(nums):
            
            check_point = target - v

            if check_point in temp_dict:
                return [temp_dict[check_point], i]
            else:
                temp_dict[v] = i

        print(f"ther is no value for {target}")


instance1 = Solution()
print(instance1.twoSum2([1, 2, 3, 4], 7))
