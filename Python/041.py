def sum_many(*nums): #변수명 앞에 *을 붙여서 여러개
    sum = 0
    for i in nums:
        sum = sum + i
    return sum

def sum_mul(sel, *nums):
    if sel == "sum":
        result = 0
        for i in nums:
            result = result + i
    elif sel == "mul":
        result = 1
        for i in nums:
            result = result * i
    return result

a= sum_many(1,2,3,4,5)
print(a)
b =sum_mul('sum', 1, 2, 3, 4, 5)
c = sum_mul('mul', 3, 2, 2)
print(b,c)
