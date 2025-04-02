import math

def pearson_correlation(x, y, n):
    # Calculate means
    sum_x = sum(x)
    sum_y = sum(y)
    mean_x = sum_x / n
    mean_y = sum_y / n
    
    # Calculate numerator and denominator components
    numerator = 0
    sum_x_squared = 0
    sum_y_squared = 0
    for i in range(n):
        diff_x = x[i] - mean_x
        diff_y = y[i] - mean_y
        numerator += diff_x * diff_y
        sum_x_squared += diff_x * diff_x
        sum_y_squared += diff_y * diff_y
    
    # Calculate correlation coefficient
    denominator = math.sqrt(sum_x_squared * sum_y_squared)
    if denominator == 0:
        return "Error: Division by zero"
    r = numerator / denominator
    return r

# Example usage:
# x = [1, 2, 3, 4]
# y = [2, 4, 6, 8]
# print(pearson_correlation(x, y, 4))