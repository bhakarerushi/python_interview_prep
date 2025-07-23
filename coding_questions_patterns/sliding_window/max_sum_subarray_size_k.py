


def max_sum_subarray(arr, k, optimal_sol = True):
    """
    - define window_sum and max_sum 
    - define start and end of window
    - move winoow over give array and calculate window_sium
    - compare window_sum with max_sum
    - return max_sum

    """

    # O(N*k)
    if not optimal_sol:
        window_sum = 0
        max_sum = 0

        if len(arr) < k:
            return -1

        for i in range(len(arr)-1):
            #    if i + k > len(arr)-1:
            #        break
            window_sum = sum(arr[i:i+k])
            if window_sum > max_sum:
                max_sum = window_sum
    else:
        # optimal solution O(N)

        window_sum = sum(arr[0:k])
        max_sum = window_sum

        for i in range(k, len(arr)): # start loop from kth element and add this kth element in window_sum and substract i-kth from window_sum

            #if we do this above we dont occure this below cond.
            # if i + k > len(arr)-1:
            #        break

            window_sum = window_sum + arr[i] - arr[i-k]

            max_sum = max(window_sum, max_sum)

    return max_sum


arr = [12,2,34,22,0,0,111]

# arr = [12]

k = 3


print('max_sum is ', max_sum_subarray(arr=arr, k=k))










