


"""
Problem: Given a list of integers and a window size k, count how many subarrays of size k have sum equal to x.
Example:
Input: arr = [1, 2, 3, 4, 2], k = 3, x = 9
Output: 1 → [2, 3, 4]

"""



# optimal solution with O(N) time complexity
# O(1) space complexcity

def subarr_with_sum_x(arr, k, x):

    sub_arr_count = 0

    window_sum = sum(arr[0:k])
    # max_sum = window_sum
    sub_arr_count = sub_arr_count + 1 if len(arr) >= k and window_sum == x else 0

    for i in range(k, len(arr)):
        
        window_sum = (window_sum - arr[i-k]) + arr[i] 
        if window_sum == x:
            sub_arr_count += 1
        
    return sub_arr_count

"""
arr = [1, 2, 3, 4, 2]
k = 3
x = 9
output - 2


arr = [1, 2]
k = 3
x = 3
Expected Output: 0 

arr = [0, 0, 0, 0, 0]
k = 3
x = 0
Expected Output: 3

arr = [-1, -2, 3, 0, 1, -1]
k = 2
x = 1
Expected Output: 1

"""

arr = [-1, -2, 3, 0, 1, -1]
k = 2
x = 1
# Expected Output: 1

count = subarr_with_sum_x(arr, k, x)
print(f'No of sub arrays with window sum {x} - {count}')