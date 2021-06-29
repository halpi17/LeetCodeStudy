class Solution:
    def mySqrt(self, x: int) -> int:
        root = 0
        while(1):
            if x >= root ** 2 and x < (root + 1) ** 2:
                return root
            root += 1


def main():
    # x = 4 # Output: 2
    # x = 8 # Output: 2
    x = 2 ** 31 -1

    solution = Solution()
    print(f"Input: x = {x}")
    print(f"Output: {solution.mySqrt(x)}")

if __name__ == "__main__":
    main()
