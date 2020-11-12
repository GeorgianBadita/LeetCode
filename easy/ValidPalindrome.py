# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start <= end:
            curr_start = s[start]
            start_ord = ord(curr_start)
            if ord('A') <= start_ord <= ord('Z'):
                start_ord += (ord('a') - ord('A'))
                curr_start = chr(start_ord)

            curr_end = s[end]
            end_ord = ord(curr_end)
            if ord('A') <= end_ord <= ord('Z'):
                end_ord += (ord('a') - ord('A'))
                curr_end = chr(end_ord)

            if not ord('a') <= ord(curr_start) <= ord('z') and not ord('0') <= ord(curr_start) <= ord('9'):
                # skip start
                start += 1
                continue
            if not ord('a') <= ord(curr_end) <= ord('z') and not ord('0') <= ord(curr_end) <= ord('9'):
                # skip end
                end -= 1
                continue
            if curr_end != curr_start:
                return False
            start += 1
            end -= 1
        return True


print(Solution().isPalindrome("0a"))
