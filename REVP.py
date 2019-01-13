def reverse_complement(dna):
    tab_ass = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([tab_ass[c] for c in reversed(dna)])

def reverse_palindromes(dna):
    results = []
    l = len(dna)
    for i in range(l):
        for j in range(4, 13):
            if i + j > l:
                continue
            s = dna[i:i+j]
            r = reverse_complement(s)
            if s == r:
                results.append((i + 1, j))
    return results

f = open("rosalind_revp.txt", "r")
data = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
data = str1.split(">")
data.remove("")

datain = ''.join(data)

results = reverse_palindromes(datain)

print("\n".join([' '.join(map(str, r)) for r in results]))
