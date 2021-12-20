class Solution:
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

if __name__ == '__main__':
    s = Solution()
    Solution.reverseString(s,["\""])
    print(len(["\""]))

