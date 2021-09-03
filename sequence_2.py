n = 7

sequence = [0, 0, 1]

for x in range(0,n):
    xr = x+2
    print(sequence[xr])
    sequence.append(sequence[xr-2]+sequence[xr-1]+sequence[xr])