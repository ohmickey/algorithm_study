class Solution(object):
    def twoSum(self, nums, target):
        # By Brute force
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                k = nums.index(target - nums[i])
                if k == i:
                    continue
                return [i,k] if i < k else [k,i]
if __name__ == '__main__':
    s = Solution()
    nums = [3,2,4]
    target = 6
    print(s.twoSum(nums, target))

