def sum_many(*args):
    sum = 0
    for i in args:
        sum=sum+i
    return sum
result = sum_many(1,2,3)
print(result)