class Solution:
    def isValid(self, s: str) -> bool:
        left_parenthesis  = ["(", "{", "["]
        right_parenthesis = [")", "}", "]"]
        parenthesis_map   = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for parenthesis in s:
            if parenthesis in left_parenthesis:
                stack.append(parenthesis_map[parenthesis])
            elif parenthesis in right_parenthesis:
                if parenthesis != stack.pop():
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
