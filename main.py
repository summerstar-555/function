# 模拟实现len
"""
def my_len(data):
    count = 0;
    for i in data:
        count += 1;
    return count;
length = my_len(input("请输入"));
print(length);
"""

# add函数
'''
def add(x,y):
    return x + y;
a = 5;
b = 7;
a = int(input("请输入第一个数："));
b = int(input("请输入第二个数："));
print(f"{a} + {b} = {add(a,b)}");
'''

# 练习：查体温
'''
def temp(num):
    if num >= 37.5:
        print("您的体温不正常")
    else:
        print("下一位")
temp(num = int(input("请输入您的体温")))
'''

# python中函数都是有返回值的。如果不写返回语句的话还是会返回none
'''
def test( ):
    a = 5;
print(f"函数默认返回值为{test()}")

'''
# 函数的说明文档.鼠标移动到函数即可查看函数文档说明
'''
def add(x,y):
    \'''
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的其中一个数字
    :return:  返回结果
    \'''
    result = x + y
    print(f"{x} + {y} = {x + y}")
    return result
add(5,9)
'''

# 函数递归
# 将1234倒着输出，也就是4321
'''
def fun1(n):
    #先 % 10，得到最右边那一位，再除10，直到n//10=0，也就是变成一位数的时候
    if n % 10 != 0:
        print(n % 10,end = ' ');
    if (n != 0):
        fun1(n // 10)
fun1(1234)
'''

# global 变量（设置全局变量，常在函数中使用）
'''
def test():
    global num;
    num = 100;
print(num);
'''

# ATM
"""
money = 50000000;
name = " "
def menu():
    global name
    print(f"{name}，您好，欢迎来到坤坤银行ATM。请选择操作：")
    print("查询余额 [输入1]")
    print("存款 [输入2]")
    print("取款 [输入3]")
    print("退出 [输入4]")
def inquire():
    global name
    print('-'*5+"查询余额"+'-'*5)
    print(f"{name}，您好，您的余额剩余：{money}")
def deposit():
    global money
    m = int(input("请输入存款金额"))
    money += m
    print(f"存款成功，余额剩余{money}")
def withdrawal():
    global money
    m = int(input("请输入取款金额"))
    money -= m
    print(f"取款成功，余额剩余{money}")
name = input("请输入姓名：")
while 1:
    menu()
    i = int(input("请输入："))
    if i == 1:
        inquire()
    elif i == 2:
        deposit()
    elif i == 3:
        withdrawal()
    else:
        break
"""

# 多重返回值
"""
def test():
    return 1,2,3
x,y,z = test()
print(x,y,z)
"""

# 传参方式
'''
def user_info(name,age,gender = '男'):
    print(f"姓名为{name},年龄为{age},性别为{gender}")

name = input("请输入姓名:")
age = int(input("请输入年龄:"))
gender = input("请输入性别:")

#位置参数
user_info(name,age,gender)

#关键字参数 - 可打乱顺序
user_info(age = age,name = name,gender = gender)

#两者混合 - 位置传参需在前面
user_info(name,age = age,gender = gender)
'''

# 缺省参数 - 默认参数 - 在声明函数时设置默认值 - 只能在后面设置
"""
def user_info(name,age,gender = '男'):
    print(f"姓名为{name},年龄为{age},性别为{gender}")
"""
'''
user_info(name = '1',age = 5)
'''

# 函数作为参数传递
"""
def compute(x,y):
    return x * y
def test():
    res = compute(1,2)
    return res
print(test(compute()))
"""

# 可以设置函数的参数类型,只会有提示的效果
'''
def count(x: int, y: int) -> int:
    z = x + y
    return z


num = count('5', '6')  # 函数规定参数为整形,但使用字符型依旧不会出错
print(num)
num = count(5, 6)
print(num)
'''

# 函数的形参使用第三方库的类型
# 声明形参的类型可以使用这个类型相应的的方法
"""
import requests


def get_small_list(self, resp: requests.Response):
    pass
"""


# 声明变量出错: 未解析的引用
"""
from multiprocessing import Value  # 
import multiprocessing.sharedctypes  # 需要加上这句代码


def fun1(shared: multiprocessing.sharedctypes.Synchronized):    # 否则这里的声明会出错
    pass


share = Value('i', 0)
print(type(share))
"""
