def countSwaps(a):
    count=0
    for i in a:
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                count+=1
    print('Array is sorted in '+str(count)+' swaps.')
    print('First Element: '+str(a[0]))
    print('Last Element: '+str(a[-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
