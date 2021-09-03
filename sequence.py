n = int(input("Enter the length of the sequence: ")) # Do not change this line

current_number = 1
prev_number = 0
prev_2_number = 0
prev_3_number = 0

for x in range(0,n):
    if x == 0: 
        print(1)
    elif x == 1:
        print(2)
    elif x == 2:
        print(3)
        current_number = 3
        prev_number = 2
        prev_2_number = 1
    else:
        prev_3_number = current_number
        current_number = current_number + prev_number + prev_2_number
        prev_2_number = prev_number
        prev_number = prev_3_number
        print(current_number)

