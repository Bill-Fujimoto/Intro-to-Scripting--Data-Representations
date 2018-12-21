def strange_sum(input_list):
    sum=0
    for num in input_list:
        if num%3==0:
            continue
        else:
            sum+=num
    return sum




print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))