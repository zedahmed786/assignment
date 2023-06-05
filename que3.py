n = 5
prev = [1,1]
prevextend = [0]*(n-2)
prev.extend(prevextend)
for i in range(1, n+1):
    curr = [0]*i
    for j in range(1, n-i+1):
        print(" ", end="")
    if i == 1:
        print("1", end="")
    elif i == 2:
        print("1 1", end="")
    else:
        curr[0] = 1
        #updating curr list
        for j in range(1, i-1):
            curr[j] = prev[j-1] + prev[j]
        curr[i-1] = 1
        
        #printing
        for j in range(0, i):
            print(curr[j], end=" ")
        
        for j in range(0, i):
            prev[j] = curr[j]
    print()