numbers=[10, 20, 30, 40, 50]
#num=sum(numbers)
#print(f"total of the numbers in the list is {num}")
#averages= num/5
#print(f"averages of the list is {averages}")

total=0
for number in numbers:
    total=total+number
print(f"total of numbers in the list is {total}")
average=total/len(numbers)
print(f"average of numbers in the list is {average}")
highest=numbers[0]
lowest=numbers[0]
for ranking in numbers:
    if ranking>highest:
        highest=ranking
    if ranking<lowest:
        lowest=ranking
print(f"Highest number is {highest}")
print(f"lowest number is {lowest}")