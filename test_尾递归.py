print("尾递归实质：将结果保存在参数中，return不返回表达式：")
def fact(n):
    return fact_item(n, 1)
def fact_item(num, pro):
    if num == 1:
        return pro
    return fact_item(num-1, num*num+pro)

print(fact(2))
