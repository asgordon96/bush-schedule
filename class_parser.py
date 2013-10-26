def get_classes():
    f = open("fall2013.txt")
    data = f.read()
    f.close()
    data = data.split('\n')
    data = [line.strip() for line in data]

    blocks = []
    classes = []
    teachers = []
    rooms = []

    rows = 44

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

    end = data[7*rows+rows:-2]
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
        name = item[1].split("(F)")[0].split("(1)")[0].strip()
        if block in classes.keys():
            classes[block].append(name)
        else:
            classes[block] = [name]
    for k in classes.keys():
        classes[k].sort()
    return classes

def save_as_csv(filename):
    data = get_classes()
    write = []
    for item in data:
        block = item[0].split()[0]
        subject = item[0].split()[1]
        class_name = item[1].split("(F)")[0].split("(1)")[0].strip()
        teacher = item[2]
        room = item[3]
        write.append(",".join([block, subject, class_name, teacher, room]))
    write = "\n".join(write)
    f = open(filename, "w")
    f.write(write)
    f.close()