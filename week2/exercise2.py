
def main():
    sample_array = [64, 25, 12, 22, 11]
    print("Original array is:", sample_array)
    selection_sort(sample_array)
    print("Sorted array is:", sample_array)




def selection_sort(arr):
    if len(arr) == 0:
        return arr
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if(min_index != i):
            arr[i], arr[min_index] = swap(arr[i], arr[min_index])
    
def swap(a, b):
    return (b, a)

if __name__ == "__main__":
    main()

"""
Counting constant time operations in Selection Sort:
Fixed: 
Line 12: 1
Line 14: n + 1
Line 15: n
Line 16: n(n+1)/2
Line 17: n(n-1)/2

Best case (already sorted):
Variable:
Line 18: 0
Line 20: 0

Total = 1 + (n + 1) + n + n(n+1)/2 + n(n-1)/2 = n^2 + 3n/2 + 2  
"""

