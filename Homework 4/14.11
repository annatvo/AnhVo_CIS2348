# Anh Vo
# 2037824
# 14.11

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers)-1):
        max_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] > numbers[max_index]:
                max_index = j
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
        for element in numbers:
            print(element, end=' ')
        print()

if __name__ == '__main__':
    num_list = [int(num) for num in input().split()]
    selection_sort_descend_trace(num_list)
