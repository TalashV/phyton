fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

numbers = list()
counts = dict()
cc = list()
for line in fh:
    line.strip()
    if line.startswith('From '):
        mstr = line.split()
#        print(mstr[5])
        cc.append(mstr[5])
#    print(cc)

for item in cc:
    #    print(item)
    data = item[0:2]
    numbers.append(data)

for number in numbers:
    counts[number] = counts.get(number, 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)
