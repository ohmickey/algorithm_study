# LeetCode 15. 3sum

[문제 출처](https://leetcode.com/problems/3sum/)

# 문제

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

>Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: \[[-1,-1,2],[-1,0,1]]

>Example 2:

Input: nums = []
Output: []

>Example 3:

Input: nums = [0]
Output: []

>Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105


# 접근 방법

- combination으로 합이 0인경우를 구하고, 반환할 때 list(set(tuple())) 을 통해 중복을 제거하고, 이중리스트 형(문제 요구사항)으로 제출하였다.
- 시간초과를 극복해내지 못했다.

---
## 2 pointer 활용 접근방법

- index 0 부터 len(num) - 1 까지 for문을 돈다.
- num 배열을 미리 sorting 해주고, for 문을 돌 때 이전값과 같은 값이면 건너뛰어서 중복을 제거한다.
- 투 포인터를 활용하여 sum이 0 보다 작으면 left += 1, else right -= 1
- 합이 0이면 anw 배열에 담는다.

# 코드(오답)

```python
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        combi = list(combinations(nums, 3))
        anw = []
        for i in range(len(combi)):
            if not sum(combi[i]):
                anw.append((combi[i]))
        return list(set(tuple(anw)))
```

# 모범 코드

``` python
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
```
# Notion 링크

[Notion : Grow Algorithm study](https://www.notion.so/15-42-53d24d63ae0848efb5bbba942f5bbcb5)
