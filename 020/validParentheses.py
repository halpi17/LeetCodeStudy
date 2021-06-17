class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {"(": ")", "{": "}", "[": "]"}
        stack = []

        if len(s) % 2 != 0:
            return False

        for parenthesis in s:
            if parenthesis in parenthesis_map.keys():
                stack.append(parenthesis_map[parenthesis])
            elif parenthesis in parenthesis_map.values():
                if not stack:
                    return False
                if parenthesis != stack.pop():
                    return False
        if stack:
            return False
        return True

def main():
    s = "()"     # Output: true
    # s = "()[]{}" # Output: true
    # s = "(["     # Output: false
    # s = "([)]"   # Output: false
    # s = "{[]}"   # Output: true

    solution = Solution()
    print(f"Input: s = \"{s}\"")
    print(f"Output: {solution.isValid(s)}")

if __name__ == "__main__":
    main()
