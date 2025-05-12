def sum_of_gp(a, r, n):
    """
    Calculate the sum of a geometric progression.

    Parameters:
    a (float): First term
    r (float): Common ratio
    n (int): Number of terms

    Returns:
    float: Sum of the GP
    """
    if r == 1:
        return a * n
    else:
        return a * (1 - r**n) / (1 - r)

# Example usage
first_term = float(input("Enter the first term (a): "))
common_ratio = float(input("Enter the common ratio (r): "))
num_terms = int(input("Enter the number of terms (n): "))

gp_sum = sum_of_gp(first_term, common_ratio, num_terms)
print(f"The sum of the GP is: {gp_sum}")
