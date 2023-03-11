class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev1 = 0
        prev2 = 1
        for i in range(2, n+1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return current

# Create an instance of the Solution class
sol = Solution()

n = int(input("Enter the value of n: "))
fib_num = sol.fib(n)
print(f"The {n}th Fibonacci number is: {fib_num}")