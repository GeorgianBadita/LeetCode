# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/

class Solution:

    def get_next_term(self, curr_term):
        next_term = ""
        curr_ind = 0
        quant = 1
        while curr_ind < len(curr_term) - 1:
            if curr_term[curr_ind] == curr_term[curr_ind + 1]:
                quant += 1
            else:
                next_term += str(quant) + curr_term[curr_ind]
                quant = 1
            curr_ind += 1
        if curr_term[-2] != curr_term[-1]:
            next_term += "1" + curr_term[-1]
        else:
            next_term += str(quant) + curr_term[-1]
        return next_term

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        if n == 3:
            return "21"
        seq = "21"
        for i in range(3, n):
            seq = self.get_next_term(seq)
        return seq


print(Solution().countAndSay(5))
