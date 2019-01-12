with open('rosalind_dna.txt') as Database_DNA:
	dna = Database_DNA.read()

count = []
for nucl in ['A', 'C', 'G', 'T']:
	count.append(str(dna.count(nucl)))

print(' '.join(count))
