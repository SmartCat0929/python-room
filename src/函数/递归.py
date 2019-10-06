#求阶乘
def fat(n):
    ret=1
    for i in range(1,n+1):
        ret =ret *i
    return ret  #无该代码，返回None
print(fat(5))
#
#
#
# #采用递归做题
def fact(n):
    if n==1:
        return 1
    return n*f(n-1)

print(fact(7))
#关于递归的特性：
# 1.调用自身函数
# 2.有一个结束条件

# 斐波那契数列(采用递归作图）
# 0 1 1 2 3 5 8 13

def fibo(n):
    if n == 1 or n == 0:
        return n
    return fibo(n - 1) + fibo(n - 2)
print(fibo(8))

# 小结：
# 1. 必须有一个明确的结束条件
# 2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
# 3. 递归效率不高，递归层次过多会导致栈溢出(在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的
# ，所以，递归调用的次数过多，会导致栈溢出。)

