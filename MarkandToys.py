def maximumToys(prices, k):
    prices.sort()
    buy=prices[0]
    count=1
    for i in range(1,len(prices)):
        buy=buy+prices[i]
        if buy<=k:
            count+=1
        else:
            break;
        
    return count


if __name__ == '__main__':
    n,k = map(int,input().split())
    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)