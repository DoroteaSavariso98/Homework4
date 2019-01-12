with open('rosalind_hamm.txt') as input_data:
	s, t = [line.rstrip('\n') for line in input_data.readlines()]

count = 0
for i in range(len(s)):
    if s[i] != t[i]:
        count += 1
print(count)
