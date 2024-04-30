def calculate_T(n):
    if n == 0:
        return 1  #T(0) = 1 
    elif n == 1:
        return 2  #T(1) = 2
    else:
        return 2 * calculate_T(n - 1) + 3 * calculate_T(n - 2)

result = []
for n in range(0, 10):
    result.append(calculate_T(n))
    print(f"T({n}) = {result[n]}")
