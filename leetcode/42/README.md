# LeetCode 42. Trapping Rain Water

[문제 출처](https://leetcode.com/problems/trapping-rain-water/)

# 문제

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

>Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

>Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


>Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105


# 접근 방법

- 가운데의 높은 벽은 그저 양쪽을 나누는 벽이다.
- 투 포인터를 활용해서 left는 ++, right는 -- 하면서
- max_left(혹은 max_right)가 포인터 진행방향 기준으로 반대방향일 때 anw 변수에 + 해주는 식으로 해결할 수 있다.

# 코드

```python
class Solution:
    def trap(self, height):
        if not height:
            return 0

        anw = 0
        left, right = 0, len(height) - 1
        left_, right_ = height[0], height[-1]

        while left < right:
            left_, right_ = max(height[left], left_), max(height[right], right_)

            if left_ <= right_:
                anw += left_ - height[left]
                left += 1
            else:
                anw += right_ - height[right]
                right -= 1
        return anw

if __name__ == '__main__':
    s = Solution()
    print(Solution.trap(s,[0,1,0,2,1,0,1,3,2,1,2,1]))
```

# 모범 코드

``` python
class Solution:
    def trap(self, height: list[int]) -> int:
        total, peak = 0, height.index(max(height))
        for elevations in (height[:peak], height[-1:peak:-1]):
            current_level = 0
            for elevation in elevations:
                current_level = max(current_level, elevation)
                total += current_level - elevation
        return total
```
# Notion 링크

[Notion : Grow Algorithm study](https://www.notion.so/15-42-53d24d63ae0848efb5bbba942f5bbcb5)
