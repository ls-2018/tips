"""
给定一个矩阵序列，找到最有效的方式将这些矩阵相乘在一起。给定表示矩阵连的数组p，使得第i个矩阵Ai的维数为p[i-1]xp[i]
输入： p= (40,20,30,10,30)
输出： 26000
有4个大小为40*20 ， 20*30   30*10  和 10*30 的矩阵，假设这四个矩阵为A，B，C，,D该函数的执行方法可一使执行乘法运算的次数最少。
A:20*30 B:30*5  C:5*60
(AB)C   执行乘法运算的次数为  （10*30*5） + （10*5*60） = 4500
A(BC)   执行乘法运算的次数为  (30*5*60)  +  (10*30*60) = 27000
"""


# 递归法
def func_1(p, i, j):
    """
    通过把括号放在第一个不同的地方来获取最小的代价，
    每个括号内可以递归地使用相同的方法来计算
    :return:
    """
    if i == j:
        return 0
    mins = 2 ** 32
    k = i
    while k < j:
        count = func_1(p, i, k) + func_1(p, k + 1, j) + p[i - 1] * p[k] * p[j]      # 两括号？
        if count < mins:
            mins = count
        k += 1
    return mins


if __name__ == '__main__':
    arr = [1, 5, 2, 4, 6]
    n = len(arr)
    print('func_1最少的乘法次数为：', func_1(arr, 1, n - 1))
