class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

def main():
    haystack = "hello"
    needle = "ll"
    # haystack = "aaaaa"
    # needle = "bba"
    # haystack = ""
    # needle = ""
    solution = Solution()
    print(f"Input: haystack = \"{haystack}\", needle = \"{needle}\"")
    print(f"Output: {solution.strStr(haystack, needle)}")

if __name__ == "__main__":
    main()
