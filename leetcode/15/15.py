from itertools import combinations
# class Solution:
#     def threeSum(self, nums):
#         if len(nums) < 3:
#             return []
#         combi = list(combinations(nums, 3))
#         anw = []
#         for i in range(len(combi)):
#             if not sum(combi[i]):
#                 combi[i] = sorted(list(combi[i]))
#                 if not combi[i] in anw:
#                     anw.append(combi[i])
#         return anw
# class Solution:
#     def threeSum(self, nums):
#         nums = sorted(nums)
#         if len(nums) < 3:
#             return []
#         combi = list(combinations(nums, 3))
#         anw = []
#         for i in range(len(combi)):
#             if not sum(combi[i]):
#                 anw.append((combi[i]))
#         return list(set(tuple(anw)))
class Solution:
    def threeSum(self, nums):
        anw = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    anw.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return anw

if __name__ == '__main__':
    s = Solution()
    print(Solution.threeSum(s,[-1,0,1,2,-1,-4]))


