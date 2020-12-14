
def SelectionSort(arr,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr

arr=list(map(int,input().split()))
n=len(arr)
print(SelectionSort(arr,n))



# def selection_sort(arr):
#     for i in range(len(arr)):
#         minimum = i
#
#         for j in range(i + 1, len(arr)):
#             # Select the smallest value
#             if arr[j] < arr[minimum]:
#                 minimum = j
#
#         # Place it at the front of the
#         # sorted end of the array
#         arr[minimum], arr[i] = arr[i], arr[minimum]
#
#     return arr


# arr=list(map(int,input().split()))
# n=len(arr)
# print(selection_sort(arr))
