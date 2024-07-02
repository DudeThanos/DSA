my_array = [7, 12, 9, 11, 3]            # 5 elements
l = len(my_array)                   # length = 5 (0..4)
print("Selection Sort")
print("Unsorted Array:", my_array)
rounds = 0

for i in range(l):                # length time runs the oter loop
    rounds += 1
    min_index = i
    # print("i= ", i)
    # From i+1 -to- length time runs the inner loop, one less value from entire array each time it runs
    # until it reaches end and exits the inner loop
    for j in range(i+1, l):
        # print("j= ", j)
        # if jth element of array is greater than j+1 postion element
        if my_array[j] < my_array[min_index]:
            min_index = j
    # Swap both the values, i becomes min_index and vice- versa
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

# Printed the sorted array
print("Sorted array:", my_array)
print("Rounds taken:", rounds)
