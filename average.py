Len = int(input("How Much Number Do You Want To Enter?"))
numbers = []
for i in range(Len):
    number = int(input(f"Enter Number { i + 1} :"))
    numbers.append(number)
    
Average = int(sum(numbers)/len(numbers))
print(f"Average Of Your Numbers Is = { Average}")