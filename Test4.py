'''while True:
    str =input()
    if len(str) >=1 and len(str) <=5:
        print(str)
        break
    else :
        pass'''

def greet(name):
    print ("Hello, "+name+". Good M")

greet('paul')

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num
num = absolute_value(2)
print(num)
print(absolute_value(-4))

def my_func():
    x=10
    print("Value inside function:",x)
x=20
my_func()
print("Value outside function : ",x)

def greet(name, msg):
    print("Hi", name + ", " + msg)

greet("Monica", "How are you")

def greet(name, msg="Hi!"):
    print("Hello", name+ ", "+msg)

greet("Kate")
greet("Kate", "How are you")

'''def greet(msg ="Hi", name):
    print("Hello", name+','+msg)

greet("kate")
greet("Kate", "How are you")'''

def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.
    If the message is not provided,
    it defaults to "Good
    morning!"
    """
    print("Hello", name + ', ' + msg)

#greet(name="1","2","3")