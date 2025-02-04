if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    b = max(arr)
    second = min(arr)

    for i in arr:
        if i == b:
            continue
        if i > second: 
            second = i
    print(second)        
        
