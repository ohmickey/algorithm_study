# LeetCode 344. Reverse String

[문제 출처](https://leetcode.com/problems/reverse-string/)

# 문제

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.


# 접근 방법

-   짝수일때, 홀수일 때를 구분하여 중간 인덱스 기준으로 Swap 한다.

# 코드

```python
    def reverseString(self, s):
        leng = len(s)
        if leng > 1:
            if leng % 2:
                front = leng // 2 - 1
                back = leng // 2 + 1
            else:
                back = leng // 2
                front = back - 1
            while front >= 0:
                s[front], s[back] = s[back], s[front]
                front -= 1
                back += 1
```

# 모범 코드

``` python
	def reverseString(self, s: List[str]) -> None:
        s[:] = list("".join(s)[::-1])
```
# Notion 링크

[Notion : Grow Algorithm study](https://www.notion.so/1-344-7da6d680638a423e92c732a6a5e363d4)
