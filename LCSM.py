f = open("rosalind_lcsm.txt", "r")
data = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
data = str1.split(">")
data.remove("")


min_str = data[0]
for i in data:
    if len(i) < len(min_str):
        min_str = i

submat = []
for i in range (0, len(min_str)):
    for j in range (i, len(min_str)+1):
        submat.append(min_str[i:j])
submat.remove('')

works = []
for i in submat:
    sub = [x for x in data if i in x]
    if (sub == data):
        works.append(i)

lengths = []
for i in works:
    lengths.append(len(i))
ind = lengths.index(max(lengths))
print(works[ind])
