def selection_sort(L):
    n=len(L)
    
    for i in range(0,n-1):
        index_min=i

        for j in range(i+1,n):
            if L[j] < L[index_min]:
                index_min = j

        if index_min != i:
                L[i],L[index_min]=L[index_min],L[i]

        print("After Sort:",L)

if __name__=="__main__":
   # L=[6,1,4,9,2]
    L= [int(x) for x in input().split()]
    print("Before Sort:",L)
    selection_sort(L)
    #print("After Sort:",L)