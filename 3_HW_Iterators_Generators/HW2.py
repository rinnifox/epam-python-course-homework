import tempfile


def merge_files_internal(fname1: str, fname2: str) -> str:
    f1 = open(fname1, 'r')
    f2 = open(fname2, 'r')

    line1 = f1.readline()
    line2 = f2.readline()

    while True:
        if line1 and line2:
            if int(line1) <= int(line2):
                yield line1
                line1 = f1.readline()
            else:
                yield line2
                line2 = f2.readline()
        else:
            if line1:
                yield line1
                line1 = f1.readline()
            elif line2:
                yield line2
                line2 = f2.readline()
            else:
                break


def merge_files(generator):
    tf = tempfile.NamedTemporaryFile(delete=False)
    name = tf.name
    with open(name, 'w') as f3:
        for elem in generator:
            f3.write(elem)
    return name
