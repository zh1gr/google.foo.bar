def solution(total_lambs):
    if total_lambs >= 10**9:
        return 0

    vdl = dl(total_lambs)
    vfl = fl(total_lambs)

    res = len(vfl) - len(vdl)

    return abs(res)

def dl(tl):
    dbl = []
    i = 0
    ttl = 0

    while i<= tl:
        v = 2**i
        dbl.append(v)
        ttl = ttl + v
        if ttl > tl:
            break
        i = i + 1

    return dbl

def fl(tl):
    fib = [1,1]
    fttl = 2
    i = 2

    while i<= tl:
        v = fib[i-1] + fib[i-2]
        fib.append(v)
        fttl = fttl + int(fib[i])
        if fttl > tl:
            break
        i = i + 1

    return fib


print(solution(143))
print(solution(10))
print(solution(123456789))