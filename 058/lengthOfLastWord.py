class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s.split():
            return 0
        return len((s.split())[-1])


def main():
    s = "Hello World" # Output: 5
    # s = " "           # Output: 0
    solution = Solution()
    print(f"Input: s = \"{s}\"")
    print(f"Output: {solution.lengthOfLastWord(s)}")

if __name__ == "__main__":
    main()
