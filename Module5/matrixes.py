import numpy as np
from colorama import Fore, Style, init

init(autoreset=True)

A = np.random.randint(1, 10, (3, 5))
B = np.random.randint(1, 10, (3, 5))

def print_colored_result(operation, result, color):
    print(f"{color}{operation}:\n{result}\n{Style.RESET_ALL}")

"""
Create 2 matrixes (3x5) A and B, and do the next operations with them and display the result in
different colors (blue, red, green, white, yellow):
"""

print_colored_result("Matrix A", A, Fore.BLUE)
print_colored_result("Matrix B", B, Fore.RED)

"""
Matrix A – transposed (x and y coordinates were changes) – the result is new matrix with
dimensions 5x3:
"""

# Transpose Matrix A
A_transposed = A.T  # Dimensions become 5x3
print_colored_result("Matrix A Transposed", A_transposed, Fore.BLUE)

"""
Rotate the Matrix A in different directions and mirrored:
"""

# Rotations and Mirroring of Matrix A
A_rot_90 = np.rot90(A)  # Rotate 90 degrees counter-clockwise
A_rot_180 = np.rot90(A, 2)  # Rotate 180 degrees
A_rot_270 = np.rot90(A, 3)  # Rotate 270 degrees counter-clockwise
A_mirrored_h = np.fliplr(A)  # Horizontal mirroring
A_mirrored_v = np.flipud(A)  # Vertical mirroring

print_colored_result("Matrix A Rotated 90°", A_rot_90, Fore.CYAN)
print_colored_result("Matrix A Rotated 180°", A_rot_180, Fore.MAGENTA)
print_colored_result("Matrix A Rotated 270°", A_rot_270, Fore.YELLOW)
print_colored_result("Matrix A Horizontally Mirrored", A_mirrored_h, Fore.GREEN)
print_colored_result("Matrix A Vertically Mirrored", A_mirrored_v, Fore.RED)
