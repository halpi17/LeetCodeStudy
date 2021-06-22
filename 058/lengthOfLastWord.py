class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_words_list = s.split()
        if not s_words_list:
            return 0
        last_word = s_words_list[-1]
        return len(last_word)


def main():
    s = "Hello World" # Output: 5
    # s = " "           # Output: 0
    solution = Solution()
    print(f"Input: s = \"{s}\"")
    print(f"Output: {solution.lengthOfLastWord(s)}")

if __name__ == "__main__":
    main()
