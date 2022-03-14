fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
rfh = fh.read()
count = 0
for line in rfh :
#	line.strip()
    if line.startswith('From') :
        print(line)
        s = line.split()
        print(s[1])
        count = count + 1
        continue

print("There were", count, "lines in the file with From as the first word")
