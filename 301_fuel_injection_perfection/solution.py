def solution(n):
    i = int(n)
    j = 0
    
    while i > 1:
        if i & 1 == 1:
            if i % 4 == 1 or i == 3:
                i -= 1
            else:
                i += 1
        else:
            i = i >> 1
        j += 1
    return i

print(solution('4'))
print(solution('15'))