fhand = open('mbox.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)