# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0
for line in fh:
    
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line=line.rstrip()
    pos=line.find(':')
    number=float(line[pos+2:])
    count+=1
    tot+=number
avg=tot/count    
print("Average spam confidence:",avg)