def quick_sort(arr,n):
    piv=arr[n-1]
    left=[]
    right=[]
    for i in arr:
        if piv>=i:
            left.append(i)
        else:
            right.append(i)
    for i in range(len(left)):
        pos=i
        cursor=left[i]
        while pos>0 and left[pos-1]>cursor:
            left[pos]=left[pos-1]
            pos=pos-1
        left[pos]=cursor
    for i in range(len(right)):
        pos=i
        cursor=right[i]
        while pos>0 and right[pos-1]>cursor:
            right[pos]=right[pos-1]
            pos=pos-1
        right[pos]=cursor
    arr=left+right
    return arr


l=list(map(int,input().split()))
n=len(l)
print(quick_sort(l,n))
