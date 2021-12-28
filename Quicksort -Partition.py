def quickSort(arr):
    p=arr[0]
    left=[]
    right=[]
    for i in range(1,len(arr)):
        if arr[i]<p:
            left.append(arr[i])
        elif arr[i]>p:
            right.append(arr[i])
    left.append(p)
    left.extend(right)
    return left

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    print(result)