def find_missing_number(arr):
    n = len(arr) + 1
    print(n)
    total_sum = n * (n + 1) // 2
    print(total_sum)
    return total_sum - sum(arr)

print(find_missing_number([ 1,2, 4, 5, 3, 7, 8,9,10]))