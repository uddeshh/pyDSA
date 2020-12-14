def merge_sort(left,right):
    arr=[]
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

    while len(left)!=0 and len(right)!=0:
        if left[0]<right[0]:
            arr.append(left[0])
            left.pop(0)
        else:
            arr.append(right[0])
            right.pop(0)
    arr=arr+left+right
    return arr

l=list(map(int,input().split()))
left=l[:int(len(l)/2)]
right=l[int(len(l)/2):]
print(merge_sort(left,right))
