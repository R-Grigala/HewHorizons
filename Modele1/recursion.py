def print_hello_world(n, max_n):
    if n > max_n:
        return
    # Print "Hello World!" followed by the current value of 'n'
    print("Hello World!", n)
    # Recursive call with incremented value of 'n'
    print_hello_world(n + 1, max_n)

print_hello_world(1, 10)