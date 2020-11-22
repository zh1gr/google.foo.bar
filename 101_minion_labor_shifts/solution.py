
def solution(data, n):
    cnt = {}
    for i in range(len(data)):
        cnt[data[i]] = cnt.get(data[i],0)+1
    for k, v in cnt.items():
        if(v > n):
            for i in range(v):
                data.remove(k)
    return data


data = [5,10,15,10,7]
print(solution(data, 1))

data = [10,2,2,3,8,4,5,11,5,8]
print(solution(data, 1))

data = [1,2,2,3,3,3,4,5,5]
print(solution(data, 1))
