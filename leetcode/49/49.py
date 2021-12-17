from collections import defaultdict

def anagrams(arr):
    lst = defaultdict(list);
    for word in arr:
        lst[''.join(sorted(word))].append(word)
    return list(lst.values())


a = ["eat","tea","tan","ate","nat","bat"]
b = anagrams(a)

print(b)
