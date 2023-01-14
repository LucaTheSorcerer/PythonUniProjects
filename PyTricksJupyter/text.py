filename = "readFileDefault.py" # this code
f = open(filename)
lines = []
for line in f:
    lines.append(line.strip())
print(lines)