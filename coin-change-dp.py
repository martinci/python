# make_change takes 2 parameters:
#   coins: array of available values of coins.
#   n: money amount.
# Return: number of ways to make change for n
def make_change(coins,n):
    l = len(coins)
    if l == 0:
        if n != 0:
            return 0
        return 1
    if (l,n) not in memory:
        max_coin = (n - n%coins[0])/coins[0] 
        max_coin = int(max_coin)
        memory[l,n] = sum([make_change(coins[1:],n - coins[0]*k) for k in range(max_coin+1)])
    return memory[l,n]


if __name__ == '__main__':
    n,m = map(int,input().strip().split())
    coins = list(map(int,input().strip().split()))
    memory = {}
    for l in range(m):
        memory[l+1,0] = 1
    print(make_change(coins,n))
