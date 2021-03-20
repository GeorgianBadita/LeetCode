# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if not S or K > len(S):
            return 0

        if K == 1:
            return len(S)

        if K == len(S) and len(set(S)) != len(S):
            return 0

        seen = {S[0]: 0}
        length = 1
        num_substrs = 0

        i = 1
        while i < len(S):
            curr_in_seen = S[i] in seen

            if not curr_in_seen:
                seen[S[i]] = i
                length += 1
            elif curr_in_seen:
                last_pos = seen[S[i]]
                length = 1
                i = last_pos + 1
                if i == len(S):
                    break
                seen = {S[i]: i}

            if length == K:
                num_substrs += 1
                del seen[S[i - K + 1]]
                length -= 1
            i += 1

        return num_substrs


print(Solution().numKLenSubstrNoRepeats("havefunonleetcode",
                                        1))
