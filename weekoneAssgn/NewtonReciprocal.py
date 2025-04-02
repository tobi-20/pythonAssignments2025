def newton_reciprocal(N, max_iterations=10, tolerance=0.000001):
    x = 0.1  # Initial guess
    print(f"Initial guess: {x}")
    
    for i in range(max_iterations):
        prev_x = x
        x = x * (2 - x * N)  # Newton's iteration formula
        error = abs(x - prev_x)
        print(f"Iteration {i}: x = {x:.8f}, Error = {error:.8f}")
        
        if error < tolerance:
            print(f"Converged after {i+1} iterations")
            break
    
    return x

# Example usage with N = 5:
N = 5
result = newton_reciprocal(N)
print(f"Final result: {result:.8f}")
print(f"Actual 1/{N} = {1/N}")