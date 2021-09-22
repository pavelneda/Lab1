def maxgold(W, wgt): 
    n=len(wgt)
    tab = [[0 for x in range(W + 1)] for x in range(n + 1)] 
 
    for i in range(n + 1): 
        for j in range(W + 1): 
            if not i or not j: 
                tab[i][j] = 0
            elif wgt[i-1] <= j: 
                tab[i][j] = max(wgt[i-1] + tab[i-1][j-wgt[i-1]],  tab[i-1][j]) 
            else: 
                tab[i][j] = tab[i-1][j] 
   
    return tab[n][W] 
W = 20
try:
    wgt = [int(i) for i in input().split()]
    print(maxgold(W, wgt))
except:
    print(None)

 