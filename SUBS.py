with open('rosalind_subs.txt') as input_data:
	s,t = input_data.readlines()
	s = s.rstrip()
	t = t.rstrip()

def findSubs(s,t):
    motifs = []
    k = 0
    while k < len(s):
        k = s.find(t, k)
        if k == -1:
            return motifs
        else:
            motifs.append(str(k+1))
            k += 1
    return motifs

subs = findSubs (s,t)
print(' '.join(subs))
