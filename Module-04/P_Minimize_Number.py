def even_checkers(arr):
    count = 0
    while True:
            for x in arr:
                if x % 2 != 0:
                    return count

            arr = [x // 2 for x in arr]
            count += 1


test_case = int(input())
arr = list(map(int, input().split() ))


if len(arr) != test_case: 
    print("Sequence length does not match the given length.")
else:
    result = even_checkers(arr)

print(result)



