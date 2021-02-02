class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        if not s:
            return True

        first_half_vowels = 0
        second_half_vowels = 0

        vowels = "AEIOUaeiou"

        for i in range(len(s) // 2):
            if s[i] in vowels:
                first_half_vowels += 1
            if s[len(s) - i - 1] in vowels:
                second_half_vowels += 1

        return second_half_vowels == first_half_vowels
