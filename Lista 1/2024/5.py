def solve(n, partial = []):
    while n > 0:
        partial.append(n & 1)
        n //= 2
    partial.reverse()
    answer = ''.join(map(str, partial))
    return answer
print(solve(int(input())))

