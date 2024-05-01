def prefix_computation(a, b):
    a = [int(digit) for digit in str(a)]
    b = [int(digit) for digit in str(b)]

    #make a and b equal length
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = [0] * (len(a) - len(b)) + b

    #prefix computation
    result = []
    carry = 0
    for i in range(len(a)-1, -1, -1):
        sum = a[i] + b[i] + carry
        result.insert(0, sum % 2)
        carry = sum // 2

    if carry:
        result.insert(0, carry)

    result = int(''.join(map(str, result)))
    return result

a = 1001
b = 0b0011
print(prefix_computation(a, b))