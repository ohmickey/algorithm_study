# LeetCode 5.가장 긴 팰린드롬 부분 문자열

[문제 출처](https://leetcode.com/problems/longest-palindromic-substring/)

# 문제

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.


# 접근 방법

-   sorted(arr[i])로 각각을 정렬한다.
-   defaultdict(list) 에 위에서 구한것을 키값으로 하는 해당 인덱스에 arr[i]를 append 시켜준다.

-   반환형이 리스트형이어야 하므로 defaultdict의 value 를 리스트에 담아 반환한다.

# 코드

```python
def anagrams(arr):
    lst = defaultdict(list);
    for word in arr:
        lst[''.join(sorted(word))].append(word)
    return list(lst.values())
```

# 모범 코드

``` python
class Solution(object):
    def longestPalindrome(self, s):
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]
        if len(s) < 2 or s == s[::-1]:
            return s
        res = ""
        for i in range(len(s)):
            odd = helper(i, i)
            even = helper(i, i+1)
            res=max(odd,res,even,key=lambda x: len(x))

        return res
```
# Notion 링크

[Notion : Grow Algorithm study](https://www.notion.so/49-4f105708cdeb413f8d85a0f05638bf17)
