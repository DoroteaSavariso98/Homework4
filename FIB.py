def Fib(n,k):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fib(n-1,k) + k*Fib(n-2, k)

with open('rosalind_fib.txt') as input_data:
	n,k = map(int, input_data.read().split())

rabbits = str(Fib(n,k))
print(rabbits)
