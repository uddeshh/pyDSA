def insertion_sort(arr,n):

    for i in range(n):
        pos=i
        cursor=arr[i]
        while pos>0 and arr[pos-1]>cursor:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=cursor
        print(arr)
    return arr

l=list(map(int,input().split()))
n=len(l)
print(insertion_sort(l,n))
