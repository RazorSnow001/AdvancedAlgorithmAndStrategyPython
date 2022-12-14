

def cut(n) -> list[list[int]]:
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]

    solutions = []
    for i in range(1, n + 1):
        if n-i == 0:
            solutions.append(i)
            continue

        subSolutions = cut(n - i)
        num = len(subSolutions)
        for j, in range(num):
            currentSubSolution = subSolutions[j]
            currentSubSolution.insert(0, i)
            solutions.append(currentSubSolution)

    return solutions


print("the solutions for cut n ", cut(2))
