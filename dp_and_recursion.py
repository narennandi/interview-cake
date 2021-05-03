class Fib():
    def __init__(self):
        self.memo = {}

    #recursion and memoization
    def fib(self, n):
        if n < 0:
            raise IndexError(
                'n cannot be negative'
            )
        
        if n in [0,1]:
            return n
        
        if n in self.memo:
            return self.memo[n]

        self.memo[n] =  self.fib(n-2) + self.fib(n-1)
        return self.memo[n]

    def fib_bottom_up(self, n):
        if n in [0,1]:
            return n

        previous_prev = 0
        prev = 1

        for _ in range(n-1):
            result = previous_prev + prev
            
            previous_prev = prev
            prev = result

        return result



if __name__ == '__main__':
    f = Fib()
    # print(f.fib(5))
    print(f.fib_bottom_up(6))