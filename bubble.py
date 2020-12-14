def bubble_sort(arr,n):
    for i in range(n):
        flag=0
        for j in range(n-i-1):
                if arr[j+1]<arr[j]:
                    arr[j+1],arr[j]=arr[j],arr[j+1]
                    flag=1
        if flag==0:
            break
    return arr

arr=list(map(int,input().split()))
n=len(arr)
print(bubble_sort(arr,n))
