class Solution(object):
    def twoSum(self, nums, target):
        new_arr = []
        sum = 0
        #Make Combination of every possible duo and check for sum to ge the indexes in new_arr
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                else:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        new_arr.append(i)
                        new_arr.append(j)
                        return new_arr
