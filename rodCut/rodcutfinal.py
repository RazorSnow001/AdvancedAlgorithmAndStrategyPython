def maxCut(n,m) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    Max = 0
    for i in range(1, n + 1):
        if n-i > len(m) and m[n-i] >= 0:
            subMax = m[n-i]
        else:
            subMax = maxCut(n - i)
        if p[i] + subMax > Max:
           Max = p[i] + subMax

    m.insert(n,Max)
    return Max

p = [0,1,5,8,9,10,17,17,20,24,30]
m = [0,1]
print(maxCut(1000,m))
