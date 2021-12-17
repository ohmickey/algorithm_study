# LeetCode 49.그룹 애너그램

[문제 출처](https://leetcode.com/problems/most-common-word/)

# 문제

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: \[["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: \[[""]]
Example 3:

Input: strs = ["a"]
Output: \[["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

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
