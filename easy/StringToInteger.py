# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

class Solution:
    def myAtoi(self, str: str) -> int:
        MIN_INT = -2 ** 31
        MAX_INT = 2 ** 31 - 1

        # if the string is empty no conversion is performed
        if not str:
            return 0

        # discard whitespaces
        curr_pos = 0
        while curr_pos < len(str) and str[curr_pos] == ' ':
            curr_pos += 1

        # if we traversed the entire string
        if curr_pos == len(str):
            return 0

        first_non_white = str[curr_pos]
        # if first nonwhite char is not a sign or digit
        if first_non_white not in '+-' and not ('0' <= first_non_white <= '9'):
            return 0

        # get the sign of the number
        sign = -1 if first_non_white == '-' else 1

        # if there is a sign skip it
        if first_non_white in '+-':
            curr_pos += 1

        # skip all leading zeros
        while curr_pos < len(str) and str[curr_pos] == '0':
            curr_pos += 1

        # create the number
        num = 0
        # while the string is not fully iterated and the current char is a digit
        while curr_pos < len(str) and '0' <= str[curr_pos] <= '9':
            # if we overflow MAX_INT
            if sign == 1 and (MAX_INT // 10 < num or (MAX_INT // 10 == num and int(str[curr_pos]) > MAX_INT % 10)):
                return MAX_INT

            # if we overflow MIN_INT
            if sign == -1 and (int(MIN_INT / 10) > -num or (
                    int(MIN_INT / 10) == -num and int(str[curr_pos]) > MAX_INT % 10 + 1)):
                return MIN_INT

            num = num * 10 + int(str[curr_pos])
            curr_pos += 1

        # return the created number
        return sign * num


print(Solution().myAtoi("-2147483649"))
