from numpy import zeros

f = open("rosalind_pdst.txt", "r")
dna_list = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
data_dna = str1.split(">")
data_dna.remove("")

dna_len = len(data_dna[0])

M = zeros((len(data_dna),len(data_dna)))
for i in range(len(data_dna)):
	for j in range(len(data_dna)):
		if i < j:
			for k in range(dna_len):
				if data_dna[i][k] != data_dna[j][k]:
					M[i][j] += 1.0/dna_len
		elif i > j:
			M[i][j] = M[j][i]

for row in range(0, len(data_dna)):
	print('\n'+(' '.join(map(str,M[row]))))

