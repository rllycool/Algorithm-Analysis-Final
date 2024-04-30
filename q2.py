def prefix_computation(a, b):
    # Convert the binary numbers to lists of integers
    a = [int(digit) for digit in str(a)]
    b = [int(digit) for digit in str(b)]

    # Pad the shorter list with zeros to make them of equal length
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = [0] * (len(a) - len(b)) + b

    # Perform prefix computation
    result = []
    carry = 0
    for i in range(len(a)-1, -1, -1):
        sum = a[i] + b[i] + carry
        result.insert(0, sum % 2)
        carry = sum // 2

    # Add the final carry if necessary
    if carry:
        result.insert(0, carry)

    # Convert the result back to a binary number
    result = int(''.join(map(str, result)))

    return result

# Example usage
a = 1010
b = 1101
result = prefix_computation(a, b)
print(result)  # Output: 10111