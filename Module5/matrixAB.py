import numpy as np
from colorama import Fore, Style, init

init(autoreset=True)

# Create matrices A and B
A = np.arange(1, 21).reshape(4, 5)
B = np.arange(20, 0, -1).reshape(4, 5)

def print_colored_result(operation, result, color):
    print(f"{color}{operation}:\n{result}\n{Style.RESET_ALL}")

# Horizontally stack A and B
AB_hstack = np.hstack((A, B))
BA_hstack = np.hstack((B, A))

# Perform matrix addition, subtraction, element-wise multiplication
sum_matrices = A + B  # Element-wise addition
diff_matrices = A - B  # Element-wise subtraction
prod_matrices = A * B  # Element-wise multiplication

# Matrix multiplication (dot product) between A and B.T
B_transposed = B.T  # Transpose of B
matrix_multiplication = A @ B_transposed  # Matrix multiplication (A * B.T)


# Vertically stack A and B
AB_vstack = np.vstack((A, B))

# Vertically stack the horizontally stacked matrices
AB_BA_vstack = np.vstack((AB_hstack, BA_hstack))  # [[A, B], [B, A]]

# Display results
print_colored_result("Matrix A (4x5)", A, Fore.BLUE)
print_colored_result("Matrix B (4x5)", B, Fore.RED)
print_colored_result("Horizontally Stacked Matrix AB (4x10)", AB_hstack, Fore.GREEN)
print_colored_result("Vertically Stacked Matrix AB (8x5)", AB_vstack, Fore.YELLOW)
print_colored_result("Horizontally Stacked [B, A] (4x10)", BA_hstack, Fore.YELLOW)
print_colored_result("Vertically Stacked [[A, B], [B, A]] (8x10)", AB_BA_vstack, Fore.CYAN)
print_colored_result("Matrix Addition (A + B)", sum_matrices, Fore.MAGENTA)
print_colored_result("Matrix Subtraction (A - B)", diff_matrices, Fore.LIGHTGREEN_EX)
print_colored_result("Element-wise Multiplication (A * B)", prod_matrices, Fore.LIGHTYELLOW_EX)
print_colored_result("Matrix Multiplication (A @ B.T)", matrix_multiplication, Fore.WHITE)
