'''# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# variable to store the sum
sum = 0
# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)

# Output : range(0, 10)
print(range(10))
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))
# Output : [2, 3, 4, 5, 6, 7]
print(list(range(2, 8)))
# Output : [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))

#print(list(range(1.5, 10, 2.5)))

genre = ['pop', 'rock', 'jazz']
# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])'''


n = int(input("Enter n: "))
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1 # update counter
    if n > 10 :
        break
# print the sum
print("The sum is", sum)

'''counter = 0
while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")'''