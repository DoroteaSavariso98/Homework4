f = open("rosalind_tran.txt", "r")
data = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
data = str1.split(">")
data.remove("")

nuc={"A":"pur","G":"pur","C":"pyr","T":"pyr"}

transition=0.0
transversion=0.0

dna1 = data[0]
dna2 = data[1]

for i in range(0,len(dna1)):
    n1 = dna1[i]
    n2 = dna2[i]
    if n1 != n2:
        if nuc[n1] == nuc[n2]:
            transition += 1
        else: transversion += 1
print(transition/transversion)
