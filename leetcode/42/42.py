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
