'''a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5
float_2 = 1.5e2
#Complex Literal
x = 3.14j
print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

"This is Python"
char = "C"
multiline_str = """This is a multiline string
with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"
print(char)
print(multiline_str)
print(unicode) # Ünicöde
print(raw_str)
'''
'''
str = 'cold'
# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = '
, list_enumerate)
#character count
print('len(str) = '
, len(str))'''

'''d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1])
print("d['key'] = ", d['key'])
# Generates error
print("d[2] = ", d['key'])'''

num_int = 123
num_str = "456"
print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))
num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))
num_sum = num_int + num_str
print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))