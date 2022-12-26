def cut(n: int) -> list[list[int]]:
    # 递归的终止条件
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]

    solutions = []
    Max = 0
    MaxSolution =[]
    # for 循环套 递归 的 DFS 范式
    for i in range(1, n + 1):
        subSolutions = cut(n - i) #[ [1,1],[2]  ] n=3
        # 拼接 i 和 下一层返回的值
        for currentSubSolution in subSolutions:
            # i = 1
            currentM = 0

            currentSubSolution.insert(0, i)  # [1,1,1] , [1,2]
            solutions.append(currentSubSolution)

            for rod in currentSubSolution:  # [1,1]
                currentM = p[rod] + currentM
            if currentM > Max:
                Max = currentM
                MaxSolution = currentSubSolution

    print("n %s , max %d  Maxsolution %s" % (n, Max,MaxSolution))
    return solutions

p = [0,1,5,8,9,10,17,17,20,24,30]
m = []
print(cut(5))
# 目前方法 ： 遍历所有可行解，然后得到价格，然后比较 -> 数学问题中， 遍历值域拿最值
# 比较低效 ， 子问题嵌套， n=3 ，n=2 ，n=1 子问题重复计算 ，存起来
# 一步一步思考的能力 ，建立在抽象之上的，先框架再填充细节，画圆理论，
# 先写注释  中文1 2 3  1  2  3
# 导数 极值点 局部的 最值点  -> 比一下这些导数为0的点还有不可导点 。。。。 最大值 ，遍历局部的最值点 ，
# m5 = 1 + m4 ,2+m3 ,3+m2 ,4+m1 ,5 - > 全部最大值  2+m3
#