num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
prev_num = 0
max_int = 0

# Find the highest number the user inputs, if they input a negative number print the highest number.
while 0 <= num_int:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: ")) 

print("The maximum is", max_int)    # Do not change this line