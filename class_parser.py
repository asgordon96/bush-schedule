import re

def get_classes(filename, rows=45):
    f = open(filename)
    data = f.read()
    f.close()
    data = data.split('\n')
    data = [line.strip() for line in data]

    blocks = []
    classes = []
    teachers = []
    rooms = []

    rows = rows
    
    for i in range(8):
        d = data[i*rows:i*rows+rows]
        if i % 4 == 0:
            blocks += d
        elif i % 4 == 1:
            classes += d
        elif i % 4 == 2:
            teachers += d
        else:
            rooms += d

    end = data[7*rows+rows:]
    n = len(end) / 4
    for i in range(4):
        d = end[i*n:i*n+n]
        if i % 4 == 0:
            blocks += d
        elif i % 4 == 1:
            classes += d
        elif i % 4 == 2:
            teachers += d
        else:
            rooms += d

    return zip(blocks, classes, teachers, rooms)
    
def classes_by_block():
    data = get_classes()
    classes = {}
    for item in data:
        block = item[0].split()[0]
        name = item[1].split("(F)")[0].split("(1)")[0].split("(W)")[0].strip()
        if block in classes.keys():
            classes[block].append(name)
        else:
            classes[block] = [name]
    for k in classes.keys():
        classes[k].sort()
    return classes

def save_as_csv(infile, filename, rows):
    data = get_classes(infile, rows)
    write = []
    for item in data:
        block = item[0].split()[0]
        subject = item[0].split()[1]
        pattern = '\(W\)|\(1\)|\(2\)|\(W\3\)|\(W\)|\(S\)'
        class_name = re.split(pattern, item[1])[0].strip()
        teacher = item[2]
        room = item[3]
        write.append(",".join([block, subject, class_name, teacher, room]))
    write = "\n".join(write)
    f = open(filename, "w")
    f.write(write)
    f.close()

if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    outfile = sys.argv[2]
    if len(sys.argv) == 4:
        rows = int(sys.argv[3])
    else:
        rows = 44
    save_as_csv(infile, outfile, rows)
    print "Saved to %s" % (outfile)