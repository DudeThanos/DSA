my_array = [7, 12, 9, 11, 3]            # 5 elements
l = len(my_array)                   # length = 5 (0..4)
print("Bubble Sort")
print("Unsorted Array:", my_array)
rounds = 1

for i in range(l-1):                # length-1 time runs the oter loop
    rounds = rounds + 1
    # length-i-1 time runs the inner loop, one less value from entire array each time it runs
    # until it reaches end and exits the inner loop
    for j in range(l-i-1):
        # if jth element of array is greater than j+1 postion element
        if my_array[j] > my_array[j+1]:
            # Swap both the values, j+1 becomes j and vice- versa
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

# Printed the sorted array
print("Sorted array:", my_array)
print("Rounds taken:", rounds-1)
