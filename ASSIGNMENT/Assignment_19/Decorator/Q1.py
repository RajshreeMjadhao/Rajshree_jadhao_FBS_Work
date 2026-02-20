# # 1. Develop a memoization decorator that caches the results of function
# # calls and returns the cached result when the same inputs occur again.
# # This can greatly improve the performance of recursive or
# # computationally intensive functions.

def memoization(fun):
    cache = {}
    def wrapper(n):
        if(n in cache):
            print('Output available.')
            return cache[n]
        output = fun(n)
        cache[n] = output
        print('Output not available.')
        return output
    

    return wrapper

@memoization
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f




