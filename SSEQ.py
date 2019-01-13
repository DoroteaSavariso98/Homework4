f = open("rosalind_sseq.txt", "r")
data = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
data = str1.split(">")
data.remove("")

seq = data[0]
sub = data[1]

start=0
indices=[]
for i in range(0,len(sub)):
    for j in range(start,len(seq)):
        if sub[i]==seq[j]:
            indices.append(j)
            start=j+1
            break

result=""
for i in indices:
    result+= str(i+1)+" "

print(result)
