from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_digits = ''.join(map(str, digits))
        plusone_string_digits = str(int(string_digits) + 1)
        return list(map(int, plusone_string_digits))


def main():
    # digits = [1, 2, 3]    # Output: [1, 2, 4]
    # digits = [4, 3, 2, 1] # Output: [4, 3, 2, 2]
    # digits = [0]          # Output: [1]
    digits = [9]          # Output: [1, 0]
    solution = Solution()
    print(f"Input: digits = {digits}")
    print(f"Output: {solution.plusOne(digits)}")

if __name__ == "__main__":
    main()
