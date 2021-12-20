# LeetCode 1. Two Sum

[문제 출처](https://leetcode.com/problems/two-sum/)

# 문제

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

# 접근 방법

-   target - nums[i] 가 nums 에 있는지 확인하고, 자기자신인지 아닌지 체크하여 아닐 시에 리스트 형 오름차순으로 리턴하였다.

# 코드

```python
class Solution(object):
    def twoSum(self, nums, target):
        # By Brute force
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                k = nums.index(target - nums[i])
                if k == i:
                    continue
                return [i,k] if i < k else [k,i]
```

# 모범 코드

```python
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		res = {}
		for idx, val in enumerate(nums):
			remn = target-val
			if remn in res:
				return [res[remn], idx]
			res[val] = idx
```

# Notion 링크

[Notion : Grow Algorithm study](https://www.notion.so/1-344-7da6d680638a423e92c732a6a5e363d4)
