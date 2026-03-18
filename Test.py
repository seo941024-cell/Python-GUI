'''num_int = 123
num_str = "456"
print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))
num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))
num_sum = num_int + num_str
print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))'''

'''a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))

def outer_function():
    # b : local
    b = 20
    def inner_func():
        # c : nested local
        c = 30
        print(a)
    inner_func()
# a : global
a = 10
outer_function()'''

'''def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)
    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a ='
, a)'''

def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =', a)
    inner_function()
    print('a =', a)   
a = 10
outer_function()
print('a =', a)


num = 3
if num > 0:
    print(num, "is a positive number.")
num = -3
if num < 0:
    print(num, "is a negative number.")

#이렇게 쓰면 귀찮으니 if, else를 쓴다.

num =3

if num >= 0:
    print(num, "은 0 또는 양수입니다.")
else:
    print("음수입니다")

num =0
if num >= 0:
    print(num, "은 양수입니다.")
elif num == 0:
    print(num, "은 0 입니다.")
else:
    print(num, "은 음수입니다.")

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")