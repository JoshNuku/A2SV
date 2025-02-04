if __name__ == '__main__':
    x = []
    y = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x.append([name,score])
        y.append(score)
    m = min(y) 
    y.sort() 
    
    for i in y:
        if i > m:
            m = i
            break
            
    l = []
    for i in x:
        if i[1] == m:
            l.append(i)
        
    l.sort()
    for i in l:
        print(i[0]) 
        
