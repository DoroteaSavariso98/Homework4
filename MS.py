def merge(a1, a2):
	c = []
	x = 0
	y = 0
	while x < len(a1) and y < len(a2):
		if a1[x] < a2[y]:
			c.append(a1[x])
			x += 1
		else:
			c.append(a2[y])
			y += 1
	if x == len(a1):
		for i in a2[y:]:
			c.append(i)
	else:
		for i in a1[x:]:
			c.append(i)
	return c

def sort(a):
	if len(a) == 1:
		return a
	else:
		return merge(sort(a[:int(len(a)/2)]), sort(a[int(len(a)/2):]))

with open('rosalind_ms.txt') as input_data:
    num = (int, input_data.readline().strip())
    list_1 = list(map(int, input_data.readline().strip().split()))

p = ""
for i in sort(list_1):
	p += str(i) + " "
print(p)
