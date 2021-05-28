class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x = str(x)[::-1]
        if str(x) == reverse_x:
            return True
        else:
            return False

def main():
    x = 123

    solution = Solution()
    print(solution.isPalindrome(x))

if __name__ == '__main__':
    main()
