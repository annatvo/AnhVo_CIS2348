#Anh Vo
#2037824
#Lab 11.18

# Get the list of integers from input
num_list = list(map(int, input().split()))

# Filter non-negative integers and sort them in ascending order
non_negative_nums = sorted(num for num in num_list if num >= 0)

# Output the non-negative integers in ascending order
for num in non_negative_nums:
    print(num, end=" ")
