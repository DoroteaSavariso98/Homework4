with open('rosalind_fibd.txt') as input:
    n,m = map(int, input.read().split())

RabbitsP = [1]+[0]*(m-1)

for year in range(1, n):
    RabbitsF = 0
    for j in range(1,m):
        RabbitsF += RabbitsP[(year-j-1)%m]
    RabbitsP[(year)%m] = RabbitsF

Tot_Rabbits = sum(RabbitsP)

print(Tot_Rabbits)
