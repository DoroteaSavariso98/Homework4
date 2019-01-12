with open('rosalind_rna.txt') as input:
	dna = input.read().strip()

with open('RNA.txt', 'w') as output:
	output.write(dna.replace('T', 'U'))
	print( dna.replace('T', 'U'))
