class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        result = ""
        carry = 0
        while any([i >= 0, j >= 0, carry != 0]):
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            result = str(carry % 2) + result
            carry //= 2
            # print(f"carry = {carry}, result = {result}")
        return result

        # 1 line Solutin
        # return bin(int(a, 2) + int(b, 2))[2:]
        # return format(int(a, 2) + int(b, 2), 'b')


def main():
    # a, b = "11", "1"      # Output: "100"
    a, b = "1010", "1011" # Output: "10101"
    solution = Solution()
    print(f"Input: a = \"{a}\", b = \"{b}\"")
    print(f"Output: {solution.addBinary(a, b)}")

if __name__ == "__main__":
    main()
