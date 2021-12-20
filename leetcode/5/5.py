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

if __name__ == '__main__':
    s = Solution()
    string = "cbbd"
    print(s.longestPalindrome)
    print(len(["\""]))
