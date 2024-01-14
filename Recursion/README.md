Recursion is a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem.

Recursion steps:
    1. Identify base case: This defines when the recursion is stops otherwise it will   go on forever.
    2. Breaking down the problem into smaller subproblems and invoking the recursive call


    For example:
        One of the most common example of recursion is the Fibonacci sequence.
        1. Base cases: fib(0) = 0 and fib(1) = 1
        2. Recurrence relation: fib(i) = fib(i-1) + fib(i-2) 

        Implementation
        ==============
        def fib(n):
            #base case
            if n <= 1:
                return n
            # recurrence relation step/ breaking it into smaller subproblems.
            return fib(n - 1) + fib(n - 2)