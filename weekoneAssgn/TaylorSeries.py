def taylor_series_sum(terms, x, a, n):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    sum_result = 0
    for i in range(n):
        term = terms[i] * ((x - a) ** i) / factorial(i)
        sum_result += term
    return sum_result

# Example usage:
# terms = [1, 1, 1]  # f(a), f'(a), f''(a)
# print(taylor_series_sum(terms, 2, 1, 3))  # x=2, a=1, n=3