class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        reverse_s = s[::-1]
        total, prev = 0, 0

        for i in reverse_s:
            if dic[i] >= prev:
                total += dic[i]
            else:
                total -= dic[i]
            prev = dic[i]

        return total

def main():
    s = "III"
    # s = "s = "IX""
    # s = "MCMXCIV"

    solution = Solution()
    print(f"Input: s = \"{s}\"")
    print("Output:", solution.romanToInt(s))

if __name__ == '__main__':
    main()