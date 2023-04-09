def largest_number(N, K):
    digits = []
    while N > 0:
        digit = N % 10
        digits.append(digit)
        N //= 10
    digits.reverse()
    result = []
    for digit in digits:
        while K > 0 and result and result[-1] < digit:
            result.pop()
            K -= 1
        result.append(digit)
    while K > 0 and result:
        result.pop()
        K -= 1
    if not result:
        return 0
    return int("".join(str(digit) for digit in result))

N = int(input().strip())
K = int(input().strip())

result = largest_number(N, K)

print(result)