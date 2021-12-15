# GROW 알고리즘 스터디 :book:
- 일시: 2021년 12월 15일 ~
- 장소: 4층 휴게실
- 방식:
    - 매일 **파이썬 알고리즘 인터뷰**에 실린 문제를 1~2문제씩 풀고 **저녁 8시**에 모여서 풀이 발표

    - **토요일 오후 1시**에 프로그래머스 문제로 테스트 및 풀이 업로드
        - Notion을 통해 코드 리뷰

## Review Template

### LeetCode 819. Most Common Word

[문제 출처](https://leetcode.com/problems/most-common-word/)

### 문제 설명

-   금지된 단어를 제외하고 가장 많이 사용된 단어를 출력하시오.
-   모든 단어는 대소문자 구분이 없으며 소문자의 형태로 반환하시오.

### 접근 방법

-   python의 `regular expression`과 `lower()` 메서드를 통해 소문자 알파벳이 아닌 character는 공백으로 바꾼다.
-   단어의 빈도수를 셀 딕셔너리를 생성하고 `banned` 단어가 아닌 경우에만 개수를 카운트한다.
-   `max(word_count,key=word_count.get)` 를 통해 딕셔너리의 가장 큰 값을 가지는 키 값을 반환한다.

### 코드

```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # drop non-alpha characters, make lower case
        words = re.sub('[^a-z]', ' ', paragraph.lower()).split()
        word_count = {}
        # count words
        for word in words:
            if word in banned:
                continue
            if not word in word_count:
                word_count[word] = 0
            word_count[word] += 1
        # get key with max value
        return (max(word_count,key=word_count.get))
```

