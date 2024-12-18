test_case = int(input())
arr = list(map(int, input().split()))

if len(arr) != test_case: 
    print("Sequence length does not match the given length.")
else:
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    removals = 0
    
    for x, count in frequency.items():
        if count > x:
            removals += count - x  
        elif count < x:
            removals += count 
    
    print(removals)

