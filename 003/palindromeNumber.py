class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

def main():
    x = 123

    solution = Solution()
    print(solution.isPalindrome(x))

if __name__ == '__main__':
    main()
