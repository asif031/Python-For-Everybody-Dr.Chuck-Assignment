name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
for lines in handle:
    if not lines.startswith("From "):
        continue
    pos=lines.find(':')
    lst.append(lines[pos-2:pos])
di=dict()
for times in lst:
    di[times]=di.get(times,0)+1
lst=sorted((k,v) for k,v in di.items())
for k,v in lst:
    print(k,v)