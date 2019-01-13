from numpy import zeros
f = open("rosalind_lcsq.txt", "r")
data = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
data = str1.split(">")
data.remove("")

dna1 = data[0]
dna2 = data[1]

def longest_common_subseq(dna1, dna2):
	Matr = zeros((len(dna1)+1,len(dna2)+1))
	for i in range(len(dna1)):
		for j in range(len(dna2)):
			if dna1[i] == dna2[j]:
				Matr[i+1][j+1] = Matr[i][j]+1
			else:
				Matr[i+1][j+1] = max(Matr[i+1][j],Matr[i][j+1])

	longest_sseq = ''
	i,j = len(dna1), len(dna2)
	while i*j != 0:
		if Matr[i][j] == Matr[i-1][j]:
			i -= 1
		elif Matr[i][j] == Matr[i][j-1]:
			j -= 1
		else:
			longest_sseq = dna1[i-1] + longest_sseq
			i -= 1
			j -= 1

	return longest_sseq

lcsq = longest_common_subseq(dna1,dna2)

print(lcsq)
