import sys
file_name = sys.argv[1]
file = open(file_name, "r")
data = file.read().split("\n")
file.close()

print(len(data))
print(data)

for x in data:
    howMany = data.count(x)
    if(howMany>1):
        where = data.index(x)+1
        for i in range(0,howMany-1):
            where = data.index(x,where)
            data.pop(where)

print(data)
print(len(data))

file = open(file_name,"w")
for x in data:
	file.write(x+"\n")
file.close()
