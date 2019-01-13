from itertools import permutations

def factorial(n):
	if n < 2:
		return 1
	else:
		return n*factorial(n-1)

with open('rosalind_perm.txt') as input_data:
	perm_set = range(1, int(input_data.read())+1)

perm_list = map(list,list(permutations(perm_set)))

print(str(factorial(len(perm_set))))

for permutation in perm_list:
	print(' '.join(map(str,permutation)))
