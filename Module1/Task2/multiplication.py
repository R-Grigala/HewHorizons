def print_mult_table(n, count=1):
    if count >10:
        return
    print(count * n, end=" ")

    print_mult_table(n, count +1)

for i in range(1, 11):
   print_mult_table(i)
   print()