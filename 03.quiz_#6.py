fib = [0, 1]
##print(fib[-2]+fib[-1])
##fib.append(3)
##print(fib)
count = 20
while count > 0:
    fib.append(fib[-2] + fib[-1])
    count -= 1
    print(fib)
    
print(fib[-1])