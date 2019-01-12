DNA = open('rosalind_revc.txt', 'r')
output = open('revc_output.txt', 'w')
line = DNA.readline().rstrip()
ComplStrand = ''
Nucleotides = list(line)
for n in Nucleotides:
    if n == 'A':
        ComplStrand += 'T'
    if n == 'T':
        ComplStrand += 'A'
    if n == 'G':
        ComplStrand += 'C'
    if n == 'C':
        ComplStrand += 'G'

rev_ComplStrand = ComplStrand[::-1]
print(rev_ComplStrand)
