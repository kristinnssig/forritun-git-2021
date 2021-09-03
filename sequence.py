n = 7 #int(input("Enter the length of the sequence: ")) # Do not change this line

current_number = 1
prev_number = 0
prev_2_number = 0
prev_3_number = 0

for x in range(0,n):
    current_number += prev_3_number + prev_2_number
    print(current_number)
    prev_3_number = prev_2_number
    prev_2_number = prev_number
    prev_number = current_number
