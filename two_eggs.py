class TwoEggs(object):
    def __init__(self):
        self.dp = [0, 1]

    def min_test_numbers(self, level):
        if level < 2:
            return self.dp[level]
        self.dp[level] = min([1 + max(i - 1, self.min_test_numbers(level - i)) for i in xrange(1, level + 1)])
        return self.dp[level]

if __name__ == '__main__':
    two_eggs = TwoEggs()
    print two_eggs.min_test_numbers(3)
# def f(n):
#     if n not in ans:
#         ans[n] = min([1+max(k-1, f(n-k)) for k in range(1, n+1)])
#     return ans[n]

# if __name__ == '__main__':
#     f(200)
#     print(ans[200])